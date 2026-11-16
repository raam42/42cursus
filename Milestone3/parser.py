import sys
from typing import Dict, List, Tuple, Set, Optional

# Assuming Zone and Connection classes are imported from a module named models
# from models import Zone, Connection

class ParseError(Exception):
    """Custom exception for all map parsing errors."""
    pass

class Network:
    """
    Acts as the container for the parsed graph environment.
    """
    def __init__(self) -> None:
        self.nb_drones: int = 0
        self.start_hub: Optional[Zone] = None
        self.end_hub: Optional[Zone] = None
        self.zones: Dict[str, Zone] = {}
        self.connections: List[Connection] = []
        self.connection_set: Set[Tuple[str, str]] = set()

class Parser:
    """
    Reads the map file, validates syntax, and builds the Object-Oriented Network.
    """
    def __init__(self, filepath: str) -> None:
        self.filepath: str = filepath
        self.network: Network = Network()
        self.parsed_first_line: bool = False

    def parse(self) -> Network:
        try:
            with open(self.filepath, 'r') as file:
                for line_num, line in enumerate(file, 1):
                    # Remove comments and whitespace[span_6](start_span)[span_6](end_span)
                    clean_line = line.split('#')[0].strip()
                    if not clean_line:
                        continue
                    
                    try:
                        self._parse_line(clean_line)
                    except ValueError as e:
                        raise ParseError(f"Error on line {line_num}: {str(e)}")
        except FileNotFoundError:
            print(f"Error: Map file '{self.filepath}' not found.", file=sys.stderr)
            sys.exit(1)

        self._validate_network()
        return self.network

    def _parse_line(self, line: str) -> None:
        # Enforce nb_drones as the first valid line[span_7](start_span)[span_7](end_span)
        if not self.parsed_first_line:
            if not line.startswith("nb_drones:"):
                raise ValueError("The first line must define 'nb_drones: <number>'")
            
            count_str = line.split(":", 1)[1].strip()
            if not count_str.isdigit() or int(count_str) <= 0:
                raise ValueError("nb_drones must be a positive integer.")
            self.network.nb_drones = int(count_str)
            self.parsed_first_line = True
            return

        if line.startswith("start_hub:") or line.startswith("end_hub:") or line.startswith("hub:"):
            self._parse_zone(line)
        elif line.startswith("connection:"):
            self._parse_connection(line)
        else:
            raise ValueError(f"Unknown declaration: {line}")

    def _extract_metadata(self, metadata_str: str) -> Dict[str, str]:
        """Extracts key=value pairs from the [metadata] bracket string."""
        meta: Dict[str, str] = {}
        if not metadata_str:
            return meta
        
        clean_str = metadata_str.strip("[] ")
        if not clean_str:
            return meta
            
        parts = clean_str.split()
        for part in parts:
            if '=' not in part:
                raise ValueError(f"Invalid metadata format, missing '=' in '{part}'")
            key, val = part.split('=', 1)
            meta[key] = val
        return meta

    def _parse_zone(self, line: str) -> None:
        prefix, rest = line.split(":", 1)
        rest = rest.strip()
        
        # Handle optional metadata brackets[span_8](start_span)[span_8](end_span)
        metadata_str = ""
        if "[" in rest and "]" in rest:
            b_start = rest.find("[")
            b_end = rest.rfind("]")
            metadata_str = rest[b_start:b_end+1]
            rest = rest[:b_start].strip()
            
        parts = rest.split()
        if len(parts) != 3:
            raise ValueError("Zone requires exactly: <name> <x> <y>")
            
        name, x_str, y_str = parts
        
        # Zone names cannot contain dashes or spaces[span_9](start_span)[span_9](end_span)
        if "-" in name:
            raise ValueError(f"Zone name '{name}' cannot contain dashes.")
        if name in self.network.zones:
            raise ValueError(f"Duplicate zone name '{name}' detected.")
            
        meta = self._extract_metadata(metadata_str)
        
        # Validate zone type if provided
        z_type = meta.get("zone", "normal")
        if z_type not in ["normal", "blocked", "restricted", "priority"]:
            raise ValueError(f"Invalid zone type '{z_type}'.")
            
        # Instantiate Zone
        is_start = prefix == "start_hub"
        is_end = prefix == "end_hub"
        zone = Zone(name, int(x_str), int(y_str), is_start, is_end)
        zone.zone_type = z_type
        zone.color = meta.get("color")
        
        if "max_drones" in meta:
            cap = meta["max_drones"]
            if not cap.isdigit() or int(cap) <= 0:
                raise ValueError("max_drones must be a positive integer.")
            # Start/End zones ignore capacity[span_10](start_span)[span_10](end_span)
            zone.max_drones = int(cap) if not (is_start or is_end) else float('inf')  # type: ignore

        if is_start:
            if self.network.start_hub is not None:
                raise ValueError("Multiple start_hub definitions found.")
            self.network.start_hub = zone
        if is_end:
            if self.network.end_hub is not None:
                raise ValueError("Multiple end_hub definitions found.")
            self.network.end_hub = zone
            
        self.network.zones[name] = zone

    def _parse_connection(self, line: str) -> None:
        rest = line.split(":", 1)[1].strip()
        
        metadata_str = ""
        if "[" in rest and "]" in rest:
            b_start = rest.find("[")
            b_end = rest.rfind("]")
            metadata_str = rest[b_start:b_end+1]
            rest = rest[:b_start].strip()
            
        if "-" not in rest:
            raise ValueError("Connection must use <name1>-<name2> format.")
            
        name1, name2 = [n.strip() for n in rest.split("-")]
        
        if name1 not in self.network.zones or name2 not in self.network.zones:
            raise ValueError(f"Connection references unknown zone(s): {name1}, {name2}")
            
        # Enforce unique bidirectional connections[span_11](start_span)[span_11](end_span)
        link_pair = tuple(sorted([name1, name2]))
        if link_pair in self.network.connection_set:
            raise ValueError(f"Duplicate connection detected between {name1} and {name2}")
            
        self.network.connection_set.add(link_pair) # type: ignore
        
        meta = self._extract_metadata(metadata_str)
        capacity = 1
        if "max_link_capacity" in meta:
            cap_str = meta["max_link_capacity"]
            if not cap_str.isdigit() or int(cap_str) <= 0:
                raise ValueError("max_link_capacity must be a positive integer.")
            capacity = int(cap_str)
            
        z1 = self.network.zones[name1]
        z2 = self.network.zones[name2]
        conn = Connection(z1, z2, capacity)
        self.network.connections.append(conn)

    def _validate_network(self) -> None:
        if self.network.start_hub is None:
            raise ParseError("Missing start_hub definition.")
        if self.network.end_hub is None:
            raise ParseError("Missing end_hub definition.")
