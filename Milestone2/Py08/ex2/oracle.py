import os
import re
import sys
import urllib.request
import urllib.error
from dotenv import load_dotenv, dotenv_values  # type: ignore


def check_security() -> None:
    """
    Runs a real environment security check by reading its own source code.
    """
    print("Environment security check:")

    with open(__file__, 'r') as file:
        source_code = file.read()
    vulnerability_pattern = (
    r'(API_KEY|DATABASE_URL|ZION_ENDPOINT)\s*=\s*[\'"][^\'"]+[\'"]'
    )

    if re.search(vulnerability_pattern, source_code):
        print("[CRITICAL] Hardcoded secrets detected in the source code!\n"
              "Security compromised. Terminating sequence.")
        sys.exit(1)
    else:
        print("[OK] No hardcoded secrets detected")
    # Check if the local .env file physically exists
    if os.path.exists('.env'):
        print("[OK] .env file properly configured")
        file_vars = dotenv_values('.env')
        active_mode = os.environ.get('MATRIX_MODE')
        file_mode = file_vars.get('MATRIX_MODE')

        if active_mode != file_mode:
            print("[OK] Active override detected!"
                  f" (File: {file_mode} -> Live: {active_mode})")
        else:
            print("[OK] Production overrides available")
    else:
        print("[WARNING] No .env file found.")
    print("\nThe Oracle sees all configurations.")


def main() -> None:
    """Main execution flow for accessing the Mainframe."""
    print("\nORACLE STATUS: Reading the Matrix...\n")
    
    # Loads the .env file. System variables take priority over .env variables.
    load_dotenv()
    
  # Fetch configurations securely from the environment
    mode = os.environ.get('MATRIX_MODE')
    db_url = os.environ.get('DATABASE_URL')
    api_base_url = os.environ.get('API_BASE_URL')
    api_key = os.environ.get('API_KEY')
    log_level = os.environ.get('LOG_LEVEL')
    zion = os.environ.get('ZION_ENDPOINT')
    
    # Graceful error handling if any configuration is completely missing
    if not all([mode, db_url, api_key, log_level, zion]):
        print("WARNING: Missing configuration detected.")
        print("Please ensure your .env file is set up or variables are exported.")
        sys.exit(1)
        
    print("Configuration loaded:\n"
          f"Mode: {mode}")
    
    # Demonstrate the difference between development and production environments
    if mode == "development":
        print("Database: Connected to local instance\n"
              f"Log Level: {log_level}")
    elif mode == "production":
        print("Database: Connected to production cluster\n"
              f"Log Level: {log_level}")
    if api_key and api_base_url:
        try:
            api_url = f"{api_base_url}?api_key={api_key}"
            urllib.request.urlopen(api_url, timeout=3)
            print("API Access: [AUTHENTICATED]")
        except urllib.error.HTTPError as e:
            if e.code == 403:
                print("API Access: [DENIED]")
            else:
                print(f"API Access: [ERROR] (HTTP Status {e.code})")
        except urllib.error.URLError as e:
            print(f"API Access: [OFFLINE] (Network error: {e.reason})")
    else:
        print("API Access: [DENIED] - Missing Connfiguration")
    

    if zion:
        try:
            # Send a GET request with a 3-second timeout so the script doesn't hang
            urllib.request.urlopen(zion, timeout=3)
            print("Zion Network: [ONLINE]\n")
        except urllib.error.URLError as e:
            # If the network is down or the URL is fake, catch the error gracefully
            print(f"Zion Network: [OFFLINE] (Reason: {e.reason})\n")
        except ValueError:
            print("Zion Network: [INVALID URL FORMAT]\n")
    else:
         print("Zion Network: [UNKNOWN]\n")
    
    check_security()


if __name__ == "__main__":
    main()