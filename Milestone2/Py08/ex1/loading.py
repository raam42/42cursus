import sys
import importlib.metadata


def check_dependencies() -> bool:
    """Checks for required packages and prints their status."""
    print("LOADING STATUS: Loading programs.\n\nChecking dependencies:")
    
    dependencies = {
        'pandas': 'Data manipulation ready',
        'numpy': 'Numerical computation ready',
        'matplotlib': 'Visualization ready'
    }
    missing_packages = []
    
    for dep, action in dependencies.items():
        try:
            # metadata.version cleanly gets the version string if installed
            version = importlib.metadata.version(dep)
            print(f"[OK] {dep} ({version}) - {action}")
        except importlib.metadata.PackageNotFoundError:
            missing_packages.append(dep)
            
    if missing_packages:
        print("\nWARNING: Missing dependencies detected\n"
              "To install using pip: pip install -r requirements.txt\n"
              "To install using Poetry: poetry install")
        return False

    return True


def run_analysis() -> None:
    """Executes the data generation and visualization."""
    # We only import these locally after confirming they are installed
    # Note: The subject allows flake8/mypy errors for these specific imports
    import numpy as np    #type: ignore # noqa
    import pandas as pd    #type: ignore # noqa
    import matplotlib.pyplot as plt    #type: ignore # noqa

    print("\nAnalyzing Matrix data...\n"
          "Processing 1000 data points...")
    
    # Generate simulated Matrix data using numpy
    matrix_data = np.random.rand(1000, 2)
    df = pd.DataFrame(matrix_data, columns=['Signal_X', 'Signal_Y'])
    
    print("Generating visualization...")
    output_file = 'matrix_analysis.png'
    # Create and save the plot
    plt.style.use('dark_background')
    plt.figure(figsize=(8, 6))
    plt.scatter(
        df['Signal_X'],
        df['Signal_Y'],
        alpha=0.8,
        c=df['Signal_Y'],
        cmap='plasma'
    )
    plt.title('Matrix Data Stream Analysis')
    plt.savefig(output_file)
    
    print("Analysis complete!\n"
          f"Results saved to: {output_file}")


def main() -> None:
    """Main execution flow."""
    if check_dependencies():
        run_analysis()
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()