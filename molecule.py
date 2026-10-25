from scapy.all import ARP, Ether, srp
import sys
import socket

INFO = "[*]"
GOOD = "[+]"
BAD = "[-]"

def banner():
    print("""
 _____         _               _     
|     |___ ___| |___ ___ _ _| |___ 
| | | | . | | | | -_|  _| | | | -_|
|_|_|_|___|___|_|___|___|___|_|___|
    network recon tool | by naughty_b0y
    """)

def arp_scan(target):
    print(f"{INFO} Starting ARP scan on ...")

def port_scan(target):
    print(f"{INFO} starting port scan on {target}...")

def banner_grab(target, port):
    print(f"{INFO} starting banner grab on {target} via port {port}...")

banner()

