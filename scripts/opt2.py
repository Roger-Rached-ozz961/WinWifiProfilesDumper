import os
import subprocess
import sys
import ctypes
import time
import logging
from tqdm import tqdm

# Function to check and relaunch the script with admin privileges
def ensure_admin():
    try:
        # Check if the script is running as admin
        is_admin = ctypes.windll.shell32.IsUserAnAdmin()
        if not is_admin:
            # Relaunch the script with admin privileges
            print("\033[33mRestarting with administrative privileges...\033[0m")
            ctypes.windll.shell32.ShellExecuteW(
                None, "runas", sys.executable, " ".join(sys.argv), None, 1
            )
            sys.exit(0)
    except Exception as e:
        print("\033[31mFailed to gain administrative privileges: \033[0m", e)
        sys.exit(1)

# Banner and About Section
def display_banner():
    print("\033[34m" + "=" * 50)
    print("Saved Wi-Fi Profiles Dumper.".center(50))
    print("=" * 50 + "\033[0m")
    print("\033[36mAuthor: Ozz961\033[0m")
    print("\033[36mDescription: Lists saved Wi-Fi profiles and saves details to a file.\033[0m")
    print("\033[34m" + "=" * 50 + "\033[0m\n")

# Function to print messages with colors
def print_colored(message, color_code):
    print(f"\033[{color_code}m{message}\033[0m")

# Setup Logging
def setup_logging(results_folder):
    log_file = os.path.join(results_folder, "wifi_profiles.log")
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
    logging.info("Script started.")

# Main logic
try:
    # Ensure script is running as admin
    ensure_admin()

    # Determine the directory where the script is located
    script_directory = os.path.dirname(os.path.realpath(__file__))

    # Prepare results folder path relative to the script directory
    results_folder = os.path.join(script_directory, "..", "results")
    os.makedirs(results_folder, exist_ok=True)

    # Setup logging
    setup_logging(results_folder)

    # Display the banner
    display_banner()

    # Create timestamped output file inside the results folder
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    username = os.getlogin()
    output_file = os.path.join(results_folder, f"wifi_profiles_{username}_{timestamp}.txt")

    print_colored("Fetching Wi-Fi profiles...", "36")
    logging.info("Fetching Wi-Fi profiles...")

    # List all Wi-Fi profiles once
    profiles_output = subprocess.check_output('netsh wlan show profiles', shell=True, text=True)
    profiles = [line.split(":")[1].strip() for line in profiles_output.splitlines() if "All User Profile" in line]

    if not profiles:
        print_colored("No Wi-Fi profiles found.", "31")
        logging.error("No Wi-Fi profiles found.")
        sys.exit(0)

    print_colored(f"Found {len(profiles)} profiles. Saving details to {output_file}", "36")
    logging.info(f"Found {len(profiles)} profiles. Saving details to {output_file}")

    # Open the file for writing results
    with open(output_file, "w", encoding="utf-8") as file:
        file.write("Wi-Fi Profiles Details:\n")
        file.write("=" * 50 + "\n")

        # Prepare commands for batch execution
        profile_commands = [f'netsh wlan show profile name="{profile}" key=clear' for profile in profiles]

        # Fetch details for all profiles with a progress bar
        for profile, command in zip(profiles, tqdm(profile_commands, desc="Processing profiles", unit="profile")):
            try:
                profile_details = subprocess.check_output(command, shell=True, text=True)

                # Extract details using parsing
                authentication = "N/A"
                key_content = "N/A"
                for line in profile_details.splitlines():
                    if "Authentication" in line:
                        authentication = line.split(":")[1].strip()
                    if "Key Content" in line:
                        key_content = line.split(":")[1].strip()

                # Write formatted details to the file
                file.write(f"SSID name          : {profile}\n")
                file.write(f"Authentication     : {authentication}\n")
                file.write(f"Key Content        : {key_content}\n")
                file.write("-" * 50 + "\n")
                print_colored(f"Details for profile {profile} saved successfully.", "32")
                logging.info(f"Details for profile {profile} saved successfully.")

            except subprocess.CalledProcessError:
                file.write(f"Error fetching details for profile: {profile}\n")
                file.write("-" * 50 + "\n")
                print_colored(f"Error fetching details for profile: {profile}", "31")
                logging.error(f"Error fetching details for profile: {profile}")

    print_colored(f"Wi-Fi profiles and details successfully saved to {output_file}.", "32")
    print_colored(f"\n\nOutput saved in: \n{output_file}", "36")
    logging.info(f"Wi-Fi profiles and details successfully saved to {output_file}.")

except subprocess.CalledProcessError:
    print_colored("Error: Unable to retrieve Wi-Fi profiles.", "31")
    print_colored("Ensure you have administrative privileges.", "33")
    logging.error("Unable to retrieve Wi-Fi profiles. Ensure you have administrative privileges.")

except KeyboardInterrupt:
    print_colored("\nOperation canceled by user. Exiting gracefully.", "33")
    logging.info("Operation canceled by user. Exiting gracefully.")
    sys.exit(0)

except Exception as e:
    print_colored(f"Unexpected error occurred: {e}", "31")
    logging.error(f"Unexpected error occurred: {e}")
    sys.exit(1)

# Pause to prevent console from closing automatically
finally:
    input("\nPress any key to exit...")
    logging.info("Script ended.")
