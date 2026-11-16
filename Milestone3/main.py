import sys
from parser import Parser, ParseError
from engine import GraphEngine
from simulation import Simulation

def main() -> None:
    """
    Main entry point for the Fly-in Drone Simulation.
    Validates arguments, initializes components, and executes the simulation.
    """
    # Ensure the user provides exactly one argument (the map file)
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_map_file.txt>", file=sys.stderr)
        sys.exit(1)

    filepath: str = sys.argv[1]

    try:
        # Phase 1: Parse the map and build the object-oriented Network
        map_parser = Parser(filepath)
        network = map_parser.parse()

        # Phase 2: Initialize the Pathfinding Graph Engine
        engine = GraphEngine(network)

        # Phase 3: Orchestrate and run the Simulation
        sim = Simulation(network, engine)
        sim.run()

    except ParseError as e:
        # Gracefully handle known parsing constraint violations
        print(f"Parse Error: {e}", file=sys.stderr)
        sys.exit(1)
    except FileNotFoundError:
        print(f"Error: Map file '{filepath}' could not be found.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        # Catch-all to gracefully avoid raw Python tracebacks crashing the evaluation[span_2](start_span)[span_2](end_span)
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
