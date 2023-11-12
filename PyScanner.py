# Leif R Bruce (00xNetrunner)
# 22.10.23
# PenTestToolkit made for Pen-testing

# This python script will use nmap and enum4linux for pen-testing
# REPORT ANY BUGS TO: leifbruce1996@zohomail.eu

import subprocess
from termcolor import colored, cprint
import time
import os


def ascii_art():
    ascii_banner = r"""
   ▄███████▄    ▄████████ ███▄▄▄▄       ███        ▄████████    ▄████████     ███         ███      ▄██████▄   ▄██████▄   ▄█          ▄█   ▄█▄  ▄█      ███     
  ███    ███   ███    ███ ███▀▀▀██▄ ▀█████████▄   ███    ███   ███    ███ ▀█████████▄ ▀█████████▄ ███    ███ ███    ███ ███         ███ ▄███▀ ███  ▀█████████▄ 
  ███    ███   ███    █▀  ███   ███    ▀███▀▀██   ███    █▀    ███    █▀     ▀███▀▀██    ▀███▀▀██ ███    ███ ███    ███ ███         ███▐██▀   ███▌    ▀███▀▀██ 
  ███    ███  ▄███▄▄▄     ███   ███     ███   ▀  ▄███▄▄▄       ███            ███   ▀     ███   ▀ ███    ███ ███    ███ ███        ▄█████▀    ███▌     ███   ▀ 
▀█████████▀  ▀▀███▀▀▀     ███   ███     ███     ▀▀███▀▀▀     ▀███████████     ███         ███     ███    ███ ███    ███ ███       ▀▀█████▄    ███▌     ███     
  ███          ███    █▄  ███   ███     ███       ███    █▄           ███     ███         ███     ███    ███ ███    ███ ███         ███▐██▄   ███      ███     
  ███          ███    ███ ███   ███     ███       ███    ███    ▄█    ███     ███         ███     ███    ███ ███    ███ ███▌    ▄   ███ ▀███▄ ███      ███     
 ▄████▀        ██████████  ▀█   █▀     ▄████▀     ██████████  ▄████████▀     ▄████▀      ▄████▀    ▀██████▀   ▀██████▀  █████▄▄██   ███   ▀█▀ █▀      ▄████▀   
                                                                                                                        ▀           ▀                          
           
           Created by 00xNetrunner

           This tool is designed to automate aspects of a pentest. Current capabilities include:
           1. Running a full Nmap scan and saving results to a text file.
           2. Running an enum4linux scan and saving results for further analysis.
           3. Executing a Hydra Brute Force attack. 

           -- Note --
           HYDRA: Requires a text file with a list of usernames in the same directory as this script.
           NMAP: For a full port scan, input '-' instead of a specific port range.
           ----------
    """
    cprint(ascii_banner, 'green')


def run_nmap(target_ip, port_range):
    nmap_command = f"nmap -vv -sV -p {port_range} {target_ip}"
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


def hydra_attack(usernameList, passwordList, attackType, targetIP, mode):
    # Adjusting Hydra command based on the mode
    if mode == 'normal':
        hydra_command = f"hydra -L {usernameList} -P {passwordList} {attackType}://{targetIP} -o crackedPasswordsFor{targetIP}.txt"
    elif mode == 'fast':
        hydra_command = f"hydra -L {usernameList} -P {passwordList} -t 20 {attackType}://{targetIP} -o crackedPasswordsFor{targetIP}.txt"
    elif mode == 'delay':
        hydra_command = f"hydra -L {usernameList} -P {passwordList} -t 4 {attackType}://{targetIP} -o crackedPasswordsFor{targetIP}.txt"

    try:
        cprint(f"Running {mode} {attackType} attack on {targetIP} with Hydra....", 'blue')
        subprocess.run(hydra_command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        cprint(f"An error occurred while running Hydra: {e}", 'red')


def main():
    ascii_art()
    cprint("Welcome to the PenTestToolkit.", 'green')
    cprint("------Scanning/Enumeration------------", 'blue')
    cprint("[1] Run full Nmap scan", 'yellow')
    cprint("[2] Run enum4linux scan", 'yellow')
    cprint("------Hydra Options------------", 'blue')
    cprint("[3] Run a normal Hydra Brute Force Attack", 'yellow')
    cprint("[4] Run a FAST Hydra Brute Force Attack", 'yellow')
    cprint("[5] Run a Hydra Brute Force delay attack | Avoid Lockout |", 'yellow')

    choice = input("Enter your choice (1/5): ")

    if choice == '1':
        target_ip = input("Enter target IP address for Nmap scan: ")
        port_range = input("Enter port range for Nmap scan (default 1-65535): ") or "1-65535"
        run_nmap(target_ip, port_range)
    elif choice == '2':
        target_ip = input("Enter target IP address for enum4linux scan: ")
        username = input("Enter the username for enum4linux scan: ")
        password = input("Enter the password for enum4linux scan: ")
        run_enum4linux(target_ip, username, password)
    elif choice in ['3', '4', '5']:
        usernameList = input("Enter the name of your username list | e.g 'users.txt' |: ")
        passwordList = input("Enter the name of your password list | e.g 'rockyou.txt |: '")
        attackType = input("What attack vector would you like to use |smb|ftp|ssh|:")
        targetIP = input("Enter the target IP address for Hydra BF attack: ")
        mode = 'normal' if choice == '3' else 'fast' if choice == '4' else 'delay'
        hydra_attack(usernameList, passwordList, attackType, targetIP, mode)
    else:
        cprint("Invalid choice, exiting...", 'red')


if __name__ == "__main__":
    main()
