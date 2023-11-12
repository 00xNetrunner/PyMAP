# PenTestToolKit
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
## Description
PyScanner is a comprehensive penetration testing toolkit designed to automate the process of network scanning and enumeration. The toolkit offers a simple and interactive menu-driven interface, empowering users to perform detailed scans using `nmap` and gather crucial information via `enum4linux`. Key features include OS detection, version scanning, banner grabbing, and user enumeration. The results from `nmap` are saved into text files while `enum4linux` output is directed into a specified text file for ease of analysis.

## Features
- Interactive menu for selecting the type of scan.
- Automated network scans with `nmap` for a range of TCP and UDP ports.
- Option to run `enum4linux` for comprehensive Windows machine enumeration.
- Customizable IP addresses, port ranges, usernames, and passwords for targeted scanning.
- Results from `nmap` are neatly organized into text files.
- `enum4linux` output is redirected to a desktop text file, `enum.txt`.

## Usage
To use PyScanner, follow the steps below:
1. Clone or download the `PyScanner.py` file from the repository.
2. Ensure you have `nmap` and `enum4linux` installed on your system.
3. Install the `termcolor` library using pip | how to set up pip: [pip4linux](https://www.tecmint.com/install-pip-in-linux/) || [pip4Win](https://www.geeksforgeeks.org/how-to-install-pip-on-windows/)
   ```bash
   pip install termcolor
   ```
4. Extract all the password lists from the .zip file, make sure they are in the same directory as the script
5. give the script permissions
   ```bash
   sudo chmod +x PyScanner.py
   ```
6. run the script:
   ```bash
   sudo python3 PyScanner.py
   ```
