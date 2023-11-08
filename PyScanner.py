# Leif R Bruce (00xNetrunner)
# 22.10.23
# PenTestToolkit made for Pen-testing

# This python script will use nmap and enum4linux for pen-testing
# REPORT ANY BUGS TO: leifbruce1996@zohomail.eu

import subprocess
from termcolor import colored, cprint

def ascii_art():
    ascii = r"""
 /$$$$$$$             /$$$$$$                                 /$$$$$$            /$$   /$$              
| $$__  $$           /$$__  $$                               /$$__  $$          |__/  | $$              
| $$  \ $$ /$$   /$$| $$  \__/  /$$$$$$$  /$$$$$$  /$$$$$$$ | $$  \__/ /$$   /$$ /$$ /$$$$$$    /$$$$$$ 
| $$$$$$$/| $$  | $$|  $$$$$$  /$$_____/ |____  $$| $$__  $$|  $$$$$$ | $$  | $$| $$|_  $$_/   /$$__  $$
| $$____/ | $$  | $$ \____  $$| $$        /$$$$$$$| $$  \ $$ \____  $$| $$  | $$| $$  | $$    | $$$$$$$$
| $$      | $$  | $$ /$$  \ $$| $$       /$$__  $$| $$  | $$ /$$  \ $$| $$  | $$| $$  | $$ /$$| $$_____/
| $$      |  $$$$$$$|  $$$$$$/|  $$$$$$$|  $$$$$$$| $$  | $$|  $$$$$$/|  $$$$$$/| $$  |  $$$$/|  $$$$$$$
|__/       \____  $$ \______/  \_______/ \_______/|__/  |__/ \______/  \______/ |__/   \___/   \_______/
           /$$  | $$                                                                                    
          |  $$$$$$/                                                                                    
           \______/  

           Created by 00xNetrunner
           
           This tool is my attempt to automate a pentest so far it can only do two things, 
           1. Run a full nmap SCAN and saves it to a text file
           2. Runs a enum4linux scan and saves it to to a text file for further viewing
    """
    cprint(ascii, 'red')

def run_nmap(target_ip, port_range):
    nmap_command = f"nmap -sV -p {port_range} {target_ip}"
    try:
        cprint(f"Running Nmap scan on {target_ip}...", 'blue')
        subprocess.run(nmap_command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        cprint(f"An error occurred while running Nmap: {e}", 'red')

def run_enum4linux(target_ip, username, password):
    enum_command = f"enum4linux -a -u {username} -p {password} {target_ip} > enum.txt"
    try:
        cprint(f"Running enum4linux on {target_ip}...", 'blue')
        subprocess.run(enum_command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        cprint(f"An error occurred while running enum4linux: {e}", 'red')

def main():
    ascii_art()
    cprint("Welcome to the PenTestToolkit.", 'green')
    cprint("[1] Run full Nmap scan", 'yellow')
    cprint("[2] Run enum4linux scan", 'yellow')

    choice = input("Enter your choice (1/2): ")
    
    if choice == '1':
        target_ip = input("Enter target IP address for Nmap scan: ")
        port_range = input("Enter port range for Nmap scan (default 1-65535): ") or "1-65535"
        run_nmap(target_ip, port_range)
    elif choice == '2':
        target_ip = input("Enter target IP address for enum4linux scan: ")
        username = input("Enter the username for enum4linux scan: ")
        password = input("Enter the password for enum4linux scan: ")
        run_enum4linux(target_ip, username, password)
    else:
        cprint("Invalid choice, exiting...", 'red')

if __name__ == "__main__":
    main()
