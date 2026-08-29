import sys
import os
import site


def is_virtual_env() -> bool:
    """
    Determines if the script is running inside a virtual environment
    by comparing the current prefix to the base prefix.
    """
    return sys.prefix != sys.base_prefix


def print_global_warning() -> None:
    """Prints the warning message for the global environment."""
    print("MATRIX STATUS: You're still plugged in\n"
          f"Current Python: {sys.executable}\n"
          "Virtual Environment: None detected\n"
          "WARNING: You're in the global environment!\n"
          "The machines can see everything you install.\n"
          "To enter the construct, run:\n"
          "python -m venv matrix_env\n"
          "source matrix_env/bin/activate  # On Unix\n"
          "matrix_env\\Scripts\\activate     # On Windows\n"
          "Then run this program again.")


def print_construct_success() -> None:
    """Prints the success message and details of the virtual environment."""
    venv_name = os.path.basename(sys.prefix)
    
    # Retrieve the path where pip will install new packages
    try:
        packages_path = site.getsitepackages()[0]
    except AttributeError:
        # Fallback for some specific environment configurations
        packages_path = os.path.join(
            sys.prefix, 'lib', 
            f'python{sys.version_info.major}.{sys.version_info.minor}', 
            'site-packages'
        )

    print("MATRIX STATUS: Welcome to the construct\n"
          f"Current Python: {sys.executable}\n"
          f"Virtual Environment: {venv_name}\n"
          f"Environment Path: {sys.prefix}\n"
          "SUCCESS: You're in an isolated environment!\n"
          "Safe to install packages without affecting the global system.\n"
          f"Package installation path: {packages_path}")


def main() -> None:
    """Main execution flow for the Construct entry sequence."""
    if is_virtual_env():
        print_construct_success()
    else:
        print_global_warning()


if __name__ == "__main__":
    main()