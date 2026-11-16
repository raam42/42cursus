import heapq
from typing import Dict, List, Tuple, Optional, Set
# from models import Zone, Connection
# from parser import Network

class GraphEngine:
    """
    Handles the pathfinding logic using a custom-weighted Dijkstra's Algorithm.
    """
    def __init__(self, network: 'Network') -> None:
        self.network = network
        # Adjacency list: zone_name -> List of (neighbor_zone, connection)
        self.adj: Dict[str, List[Tuple['Zone', 'Connection']]] = self._build_adjacency_list()

    def _build_adjacency_list(self) -> Dict[str, List[Tuple['Zone', 'Connection']]]:
        """Maps out the network for rapid neighbor lookups."""
        adj: Dict[str, List[Tuple['Zone', 'Connection']]] = {name: [] for name in self.network.zones}
        
        for conn in self.network.connections:
            z1 = conn.zone1
            z2 = conn.zone2
            adj[z1.name].append((z2, conn))
            adj[z2.name].append((z1, conn))
            
        return adj

    def _get_zone_weight(self, zone: 'Zone') -> float:
        """
        Translates zone types into mathematical weights for Dijkstra.
        Priority is slightly less than normal to guarantee it is favored[span_2](start_span)[span_2](end_span).
        """
        if zone.zone_type == "blocked":
            return float('inf')
        elif zone.zone_type == "priority":
            return 0.9  # Preferred over normal, but practically 1 turn[span_3](start_span)[span_3](end_span)
        elif zone.zone_type == "restricted":
            return 2.0  # Costs 2 turns[span_4](start_span)[span_4](end_span)
        else:
            return 1.0  # Normal zone, 1 turn[span_5](start_span)[span_5](end_span)

    def find_shortest_path(self, start_zone: 'Zone', end_zone: 'Zone', ignored_zones: Optional[Set[str]] = None) -> Optional[List['Zone']]:
        """
        Calculates the optimal path from start to end.
        Accepts an optional set of ignored_zones to dynamically find alternative paths.
        """
        if ignored_zones is None:
            ignored_zones = set()

        # Priority queue stores tuples of (cumulative_weight, zone_name)
        pq: List[Tuple[float, str]] = []
        heapq.heappush(pq, (0.0, start_zone.name))
        
        # Track shortest known distances to each zone
        distances: Dict[str, float] = {name: float('inf') for name in self.network.zones}
        distances[start_zone.name] = 0.0
        
        # Track the optimal previous zone to reconstruct the path later
        came_from: Dict[str, Optional['Zone']] = {name: None for name in self.network.zones}

        while pq:
            current_weight, current_name = heapq.heappop(pq)
            current_zone = self.network.zones[current_name]

            # If we reached the destination, reconstruct and return the path
            if current_zone == end_zone:
                return self._reconstruct_path(came_from, current_zone)

            # Optimization: If we found a shorter path previously, skip
            if current_weight > distances[current_name]:
                continue

            for neighbor, connection in self.adj[current_name]:
                if neighbor.name in ignored_zones or neighbor.zone_type == "blocked":
                    continue

                weight = self._get_zone_weight(neighbor)
                new_distance = current_weight + weight

                if new_distance < distances[neighbor.name]:
                    distances[neighbor.name] = new_distance
                    came_from[neighbor.name] = current_zone
                    heapq.heappush(pq, (new_distance, neighbor.name))

        return None  # No valid path found

    def _reconstruct_path(self, came_from: Dict[str, Optional['Zone']], current: 'Zone') -> List['Zone']:
        """Backtracks from the end zone to the start zone to build the path array."""
        path: List['Zone'] = []
        while current is not None:
            path.append(current)
            current = came_from[current.name] # type: ignore
        path.reverse()
        return path
