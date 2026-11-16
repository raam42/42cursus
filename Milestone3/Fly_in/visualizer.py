import pygame
import sys
from typing import Tuple, Dict
# from models import Zone, Drone
# from parser import Network

class Visualizer:
    """
    Handles the 2D Pygame rendering of the drone network and simulation state.
    """
    def __init__(self, network: 'Network', width: int = 1024, height: int = 768, fps: int = 2) -> None:
        self.network = network
        self.width = width
        self.height = height
        self.fps = fps
        self.margin = 100
        
        # Color Palettes
        self.colors: Dict[str, Tuple[int, int, int]] = {
            "start": (50, 205, 50),     # Green
            "end": (255, 215, 0),       # Yellow
            "normal": (200, 200, 200),  # Light Gray
            "priority": (65, 105, 225), # Royal Blue
            "restricted": (220, 20, 60),# Crimson Red
            "blocked": (105, 105, 105), # Dark Gray
            "drone": (0, 255, 255),     # Cyan
            "text": (255, 255, 255),    # White
            "line": (100, 100, 100)     # Dim Gray
        }
        
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Fly-in 42: Simulation Visualizer")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("monospace", 16, bold=True)
        
        # Calculate dynamic scaling to fit any map size on screen
        self._calculate_scaling()

    def _calculate_scaling(self) -> None:
        """Determines the coordinate multiplier based on the map's bounding box."""
        xs = [z.x for z in self.network.zones.values()]
        ys = [z.y for z in self.network.zones.values()]
        
        self.min_x, self.max_x = min(xs), max(xs)
        self.min_y, self.max_y = min(ys), max(ys)
        
        range_x = max(1, self.max_x - self.min_x)
        range_y = max(1, self.max_y - self.min_y)
        
        self.scale_x = (self.width - 2 * self.margin) / range_x
        self.scale_y = (self.height - 2 * self.margin) / range_y

    def _get_screen_coords(self, x: int, y: int) -> Tuple[int, int]:
        """Translates abstract map coordinates to physical screen pixels."""
        screen_x = int(self.margin + (x - self.min_x) * self.scale_x)
        screen_y = int(self.margin + (y - self.min_y) * self.scale_y)
        return screen_x, screen_y

    def handle_events(self) -> None:
        """Processes Pygame window events to prevent freezing."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

    def render(self, turn_number: int, drones: list['Drone']) -> None:
        """Draws the current simulation frame."""
        self.handle_events()
        self.screen.fill((20, 20, 30))  # Dark background
        
        self._draw_connections()
        self._draw_zones()
        self._draw_drones(drones)
        self._draw_ui(turn_number)
        
        pygame.display.flip()
        self.clock.tick(self.fps)  # Pause here so humans can watch the moves

    def _draw_connections(self) -> None:
        for conn in self.network.connections:
            start_pos = self._get_screen_coords(conn.zone1.x, conn.zone1.y)
            end_pos = self._get_screen_coords(conn.zone2.x, conn.zone2.y)
            # Thicker lines for higher capacity edges
            thickness = 2 + conn.max_link_capacity
            pygame.draw.line(self.screen, self.colors["line"], start_pos, end_pos, thickness)

    def _draw_zones(self) -> None:
        for zone in self.network.zones.values():
            pos = self._get_screen_coords(zone.x, zone.y)
            
            # Determine correct color based on zone type or start/end flag
            color = self.colors.get(zone.zone_type, self.colors["normal"])
            if zone.is_start:
                color = self.colors["start"]
            elif zone.is_end:
                color = self.colors["end"]
                
            pygame.draw.circle(self.screen, color, pos, 25)
            
            # Draw zone name below the node
            label = self.font.render(zone.name, True, self.colors["text"])
            self.screen.blit(label, (pos[0] - label.get_width() // 2, pos[1] + 30))

    def _draw_drones(self, drones: list['Drone']) -> None:
        # Dictionary to track how many drones are stacked in the same location to offset them visually
        location_counts: Dict[str, int] = {}
        
        for drone in drones:
            if drone.current_zone:
                # Drone is safely in a zone
                base_pos = self._get_screen_coords(drone.current_zone.x, drone.current_zone.y)
                loc_key = drone.current_zone.name
            elif drone.transit_connection:
                # Drone is mid-flight on a restricted connection (draw halfway)
                z1 = drone.transit_connection.zone1
                z2 = drone.transit_connection.zone2
                p1 = self._get_screen_coords(z1.x, z1.y)
                p2 = self._get_screen_coords(z2.x, z2.y)
                base_pos = ((p1[0] + p2[0]) // 2, (p1[1] + p2[1]) // 2)
                loc_key = f"transit_{z1.name}_{z2.name}"
            else:
                continue

            # Offset slightly if multiple drones share the exact same pixel
            offset = location_counts.get(loc_key, 0) * 10
            location_counts[loc_key] = location_counts.get(loc_key, 0) + 1
            
            final_pos = (base_pos[0] + offset, base_pos[1] - offset)
            
            # Draw Drone Marker
            pygame.draw.circle(self.screen, self.colors["drone"], final_pos, 8)
            # Draw Drone ID
            id_label = self.font.render(drone.drone_id, True, (255, 255, 0))
            self.screen.blit(id_label, (final_pos[0] + 10, final_pos[1] - 10))

    def _draw_ui(self, turn_number: int) -> None:
        turn_label = self.font.render(f"Turn: {turn_number}", True, self.colors["text"])
        self.screen.blit(turn_label, (20, 20))
