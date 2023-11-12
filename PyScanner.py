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
           3. Runs a Hydra Brtue Force attack. 
           
           -- Note --
           HYDRA
           When running the hydra atack you will need to create a text file with a list of usernames. make sure this 
           list is in the same directory as the script, you are welcome to edit the script to change it so that it scans
           one username, password lists are included when you download this script. 
           
           NMAP
           if you want to run a scan of all the ports on nmap just input - instead of a port range!
           ----------
           
    """
    cprint(ascii, 'red')

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

def hydra_normal(usernameList, passwordList, attackType, targetIP):
    # Change -L to -l if you want to bruteforce a single user.
    hydra_command = f"hydra -L {usernameList} -P {passwordList} {attackType}://{targetIP} -o crackedPasswordsFor{targetIP}.txt"
    try:
        cprint(f"Running {attackType} attack on {targetIP} with Hydra....", 'blue')
        subprocess.run(hydra_command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        cprint(f"An error occurred while running Hydra: {e}", 'red')

def hydra_fast(usernameList, passwordList, attackType, targetIP):
    # Change -L to -l if you want to bruteforce a single user.
    # Change -t 16 to a value of your choice, make sure you system can handle it,
    # if its to high it could crash the server/VM
    hydra_command = f"hydra -L {usernameList} -P {passwordList} -t 20 {attackType}://{targetIP} -o crackedPasswordsFor{targetIP}.txt"
    try:
        cprint(f"Running {attackType} attack on {targetIP} with Hydra....", 'blue')
        subprocess.run(hydra_command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        cprint(f"An error occurred while running Hydra: {e}", 'red')

def hydra_delay(usernameList, passwordList, attackType, targetIP):
    # Change -L to -l if you want to bruteforce a single user.
    hydra_command = f"hydra -L {usernameList} -P {passwordList} {attackType}://{targetIP} -o crackedPasswordsFor{targetIP}.txt"
    try:
        cprint(f"Running delayed {attackType} attack on {targetIP} with Hydra....", 'blue')
        subprocess.run(hydra_command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        cprint(f"An error occurred while running Hydra: {e}", 'red')
    sleep_interval = 5 # Change this to you desired level
    attempts = 10 # Change if you need to

    for attempt in range(attempts):
        cprint(f"Attempt {attempt + 1} of {attempts}", 'blue')
        os.system(hydra_command)
        time.sleep(sleep_interval)

    cprint("Script Completed!", 'green')

def main():
    ascii_art()
    cprint("Welcome to the PenTestToolkit.", 'green')
    cprint("------Scanning/Enumeration------------", 'purple')
    cprint("[1] Run full Nmap scan", 'yellow')
    cprint("[2] Run enum4linux scan", 'yellow')
    cprint("------Hydra Options------------", 'purple')
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
    elif choice == '3':
        usernameList = input("Enter the name of your username list | e.g 'users.txt' |: ")
        passwordList = input("Enter the name of your password list | e.g 'rockyou.txt |: '")
        attackType = input("What attack vector would you like to use |smb|ftp|ssh|:")
        targetIP = input("Enter the target IP address for Hydra BF attack")
        hydra_normal(usernameList, passwordList, attackType, targetIP)
    elif choice == '4':
        usernameList = input("Enter the name of your username list | e.g 'users.txt' |: ")
        passwordList = input("Enter the name of your password list | e.g 'rockyou.txt |: '")
        attackType = input("What attack vector would you like to use |smb|ftp|ssh|:")
        targetIP = input("Enter the target IP address for Hydra BF attack")
        hydra_fast(usernameList, passwordList, attackType, targetIP)
    elif choice == '5':
        usernameList = input("Enter the name of your username list | e.g 'users.txt' |: ")
        passwordList = input("Enter the name of your password list | e.g 'rockyou.txt |: '")
        attackType = input("What attack vector would you like to use |smb|ftp|ssh|:")
        targetIP = input("Enter the target IP address for Hydra BF attack")
        hydra_delay(usernameList, passwordList, attackType, targetIP)
    else:
        cprint("Invalid choice, exiting...", 'red')

if __name__ == "__main__":
    main()
