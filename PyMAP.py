# Leif R Bruce (00xNetrunner)
# 22.10.23
# PyMAP Scanner made for Pen-testing

# This python script will use nmap to fully scan a network
# REPORT ANY BUGS TO: leifbruce1996@zohomail.eu

import subprocess


def asciiArt():
    ascii = r"""
 /$$$$$$$            /$$      /$$  /$$$$$$  /$$$$$$$ 
| $$__  $$          | $$$    /$$$ /$$__  $$| $$__  $$
| $$  \ $$ /$$   /$$| $$$$  /$$$$| $$  \ $$| $$  \ $$
| $$$$$$$/| $$  | $$| $$ $$/$$ $$| $$$$$$$$| $$$$$$$/
| $$____/ | $$  | $$| $$  $$$| $$| $$__  $$| $$____/ 
| $$      | $$  | $$| $$\  $ | $$| $$  | $$| $$      
| $$      |  $$$$$$$| $$ \/  | $$| $$  | $$| $$      
|__/       \____  $$|__/     |__/|__/  |__/|__/      
           /$$  | $$                                 
          |  $$$$$$/                                 
           \______/
           
        Created By 00xNetrunner                                  
    """

    print(ascii)

asciiArt()


def nmapScan(scan_type, port_range, additional_flags, output_file, target_ip):
    try:
        command = f"nmap {scan_type} -p {port_range} {additional_flags} -oN {output_file} {target_ip}"
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running NMAP command: {e}")


# Prompts user for IPs to scan
userInput = input("Please enter the IPs you'd like to scan, separated by a comma: ")
ips_to_scan = [ip.strip() for ip in userInput.split(",")]

# TCP Scan settings
tcp_scan_type = "-sT"
tcp_port_range = "1-10000"
tcp_additional_flags = "-v -v -T5 -sV -O --osscan-guess --max-retries 2 --script=banner,vuln --reason"

# UDP Scan settings
udp_scan_type = "-sU"
udp_port_range = "1-500"
udp_additional_flags = "-v -v --scan-delay 1s --max-retries 2 -sV --script=banner --reason"

for ip in ips_to_scan:
    tcp_output_file = f"{ip}TCP.txt"
    udp_output_file = f"{ip}UDP.txt"

    print(f"RUNNING TCP SCAN ON {ip}")
    nmapScan(tcp_scan_type, tcp_port_range, tcp_additional_flags, tcp_output_file, ip)

    print(f"RUNNING UDP SCAN ON {ip}")
    nmapScan(udp_scan_type, udp_port_range, udp_additional_flags, udp_output_file, ip)
