import subprocess
import sys
from colorama import init

# Initialize colorama for Windows compatibility
init(autoreset=True)

# Banner and About Section
def display_banner():
    print("\033[38;5;229m" + "=" * 70)  # Light Purple color for the banner
    print(" " * 15 + "\033[38;5;226mWi-Fi Password Retrieval Script\033[0m" + " " * 15)
    print("=" * 70 + "\033[0m")
    print("\033[38;5;223m" + "Author: Roger (Ozz961)" + "\033[0m")
    print("\033[38;5;223m" + "\nDescription: This script retrieves and displays specific Wi-Fi Password" + "\nfor a user-specified Wi-Fi network." + "\n\nMake sure to run with administrative privileges to view the details.\n\nKindly Note: 'Key Content' is the password field.\n" + "\033[0m")
    print("\033[38;5;229m" + "=" * 70 + "\033[0m\n")
    print("\033[38;5;196m" + "Disclaimer: " + "\033[0m" + "\033[38;5;220m" + "USE THIS SCRIPT ONLY ON NETWORKS THAT YOU OWN OR HAVE PERMISSION TO ACCESS! 🚨\nUNAUTHORIZED ACCESS TO NETWORKS IS ILLEGAL AND UNETHICAL!!! 🚨\nBY RUNNING THIS SCRIPT, YOU AGREE TO TAKE FULL RESPONSIBILITY FOR ITS USAGE!" + "\033[0m\n")

# Function to print messages with colors
def print_colored(message, color_code):
    print(f"\033[{color_code}m{message}\033[0m")

# Graceful exit on KeyboardInterrupt
try:
    # Display the banner
    display_banner()

    # Keep the script running until the user decides to quit
    while True:
        # Get Wi-Fi network name from user input
        network_name = input("\033[38;5;226mEnter the Wi-Fi network name (or type 'exit' to quit): \033[0m").strip()

        if network_name.lower() == "exit":
            print_colored("\n\033[38;5;220mScript has been ended by the user, exiting...\033[0m", "33")
            break

        if not network_name:
            print_colored("\033[38;5;196mError: Wi-Fi network name cannot be empty!\033[0m", "31")
            continue

        # Command to run
        command = f'netsh wlan show profile name="{network_name}" key=clear'

        try:
            # Run the command and capture the output
            result = subprocess.check_output(command, shell=True, text=True)

            # Extract only the required details
            lines = result.splitlines()
            details = {}
            for line in lines:
                if "Authentication" in line:
                    details["Authentication"] = line.split(":")[1].strip()
                if "SSID name" in line and "name" in line:
                    details["SSID name"] = line.split(":")[1].strip()
                if "Key Content" in line:
                    details["Key Content"] = line.split(":")[1].strip()

            # Check if the required details exist for the given network name
            if "Authentication" in details and "SSID name" in details and "Key Content" in details:
                # Output the results to terminal with light colors
                print_colored(f"\033[38;5;118mSSID name          : {details['SSID name']}\033[0m", "32")
                print_colored(f"\033[38;5;118mAuthentication     : {details['Authentication']}\033[0m", "32")
                print_colored(f"\033[38;5;118mKey Content        : {details['Key Content']}\033[0m", "32")
                print("\033[38;5;229m" + "=" * 70 + "\033[0m")  # Light Purple separator line
            else:
                print_colored(f"\033[38;5;196mError: Could not retrieve complete details for '{network_name}'.\033[0m", "31")

        # Script Exceptions 
        except subprocess.CalledProcessError:
            print_colored(f"\033[38;5;196mError: Unable to retrieve details for '{network_name}'.\033[0m", "31")
            print_colored("\033[38;5;220mMake sure the network name is correct and you have administrative privileges.\033[0m", "33")

except KeyboardInterrupt:
    print_colored("\n\033[38;5;220mOperation canceled by user. Exiting gracefully.\033[0m", "33")
    sys.exit(0)

except Exception as e:
    print_colored(f"\033[38;5;196mUnexpected error occurred: {e}\033[0m", "31")
    sys.exit(1)
