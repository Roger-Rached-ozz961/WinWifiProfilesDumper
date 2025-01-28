# WinWifiProfilesDumper

**WinWifiProfilesDumper** is a Python-powered tool with a **WinWifiProfilesDumper.bat** wrapper, designed to help users retrieve Wi-Fi passwords and profile details on Windows systems.

## Purpose

This tool is intended for network administrators and users who need to retrieve Wi-Fi passwords and network details of Wi-Fi profiles saved on a Windows system. It helps in recovering Wi-Fi passwords for networks that the user has previously connected to.

### tool options

1. **Specific Wi-Fi Password Retrieval**  
   Retrieve the password for a user-specified Wi-Fi network SSID.
   
2. **All Saved Wi-Fi Profiles Dumper**  
   Dumps all saved Wi-Fi profiles (including passwords) to a results folder for later review.
   
3. **Credits/Author**  
   Displays information about the author and credits.
   
4. **Exit**  
   Gracefully exits the tool.

## Usage

To use the tool, run the `WinWifiProfilesDumper.bat` file. After execution, you will be presented with the following options:

1. **Retrieve Specific Wi-Fi Password**  
   Choose this option to retrieve the password for a specific Wi-Fi network by entering its name.

2. **Dump All Saved Wi-Fi Profiles**  
   Choose this option to dump all saved Wi-Fi profiles to a results folder. Check the folder for the dumped profiles and their details. (needs admin priv, file format wifi_profiles_[LOCAL_USERNAME]_[TIMESTAMP].txt)

3. **Credits/Author Information**  
   View information about the author and credits.

4. **Exit**  
   Exit the tool gracefully.

**Important**: If you choose option 2 to dump all profiles, make sure to check your results folder for the dumped profiles.

### How to get it Running.

1. Download or clone this repository to your local machine.
2. Ensure that Python 3.x is installed on your system.
3. Run `WinWifiProfilesDumper.bat` as an administrator to execute the tool.
4. Follow the on-screen instructions to choose the desired option.

## Requirements

- **Python 3.x**
- **Windows OS**
- Administrative privileges (required for retrieving Wi-Fi details)

## Disclaimer

> **WARNING: USE ONLY ON NETWORKS YOU OWN OR HAVE EXPLICIT PERMISSION TO ACCESS!**  
> Unauthorized access to networks is illegal and unethical. By using this tool, you agree to take full responsibility for its usage. The author does not take responsibility for any illegal or unethical activities that may arise from using this tool.  
>  
> This tool is intended for educational purposes, network management, and recovery of Wi-Fi credentials for networks you own or have explicit permission to access.  
> **Any misuse of this tool for unauthorized access is strictly prohibited and could result in legal consequences.**

> **By using this tool, you agree to use it responsibly and legally.**

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

## Author

This tool was created by **Roger Rached /or Ozz961**.

### Contact

- Email: [roger.contact@example.com](mailto:roger.contact@example.com)

---

## In Summary:

- Make sure you run this tool with administrative privileges for it to work correctly.
- The results folder (for option 2) will contain a text file with details of all the saved Wi-Fi profiles, including their passwords.
- Use this tool responsibly and ensure that you're only accessing networks you are authorized to access.

---

Feel free to contact the author via the provided contact details for any questions or feedback.
