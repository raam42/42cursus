import sys
import importlib.metadata


def check_dependencies() -> bool:
    """Checks for required packages and prints their status."""
    print("LOADING STATUS: Loading programs.\nChecking dependencies:")
    
    dependencies = ['pandas', 'numpy', 'requests', 'matplotlib']
    missing_packages = []
    
    for dep in dependencies:
        try:
            # metadata.version cleanly gets the version string if installed
            version = importlib.metadata.version(dep)
            print(f"[OK] {dep} ({version})")
        except importlib.metadata.PackageNotFoundError:
            missing_packages.append(dep)
            
    if missing_packages:
        print("\nWARNING: Missing dependencies detected!")
        print("To install using pip:")
        print("  pip install -r requirements.txt")
        print("To install using Poetry:")
        print("  poetry install")
        return False
        
    print("\nData manipulation ready")
    print("Numerical computation ready")
    print("Network access ready")
    print("Visualization ready\n")
    return True


def run_analysis() -> None:
    """Executes the data generation and visualization."""
    # We only import these locally after confirming they are installed
    # Note: The subject allows flake8/mypy errors for these specific imports
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    print("Analyzing Matrix data...")
    print("Processing 1000 data points...")
    
    # Generate simulated Matrix data using numpy
    matrix_data = np.random.rand(1000, 2)
    df = pd.DataFrame(matrix_data, columns=['Signal_X', 'Signal_Y'])
    
    print("Generating visualization...")
    
    # Create and save the plot
    plt.figure(figsize=(8, 6))
    plt.scatter(df['Signal_X'], df['Signal_Y'], alpha=0.5, color='0.2')
    plt.title('Matrix Data Stream Analysis')
    plt.savefig('matrix_analysis.png')
    
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    """Main execution flow."""
    if check_dependencies():
        run_analysis()
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()