import sys
import alchemy


if __name__ == "__main__":
    print("=== Alembic 4 ===\n"
          "Accessing the alchemy module using 'import alchemy'\n"
          f"Testing create_air: {alchemy.create_air()}\n"
          "Now show that not all functions can be reached\n"
          "This will raise and exception!\n"
          "Testing the hidden create_earth: ", end="")
    sys.stdout.flush()
    print(f"{alchemy.create_earth()}")  # type: ignore[attr-defined]
