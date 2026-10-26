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
    print(f"{INFO} Starting ARP scan on {target}...")
    print(f"{'IP':<20} MAC")
    print("-" * 30)

    arp = ARP(pdst=target)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp

    result = srp(packet, timeout=3, verbose=False)[0]

    for sent, received in result:
        print(f"{received.psrc:<20} {received.hwsrc}")

    print(f"\n {INFO} ARP scan completed on {target}. \n {len(result)} hosts found.")

def port_scan(target):
    print(f"{INFO} starting port scan on {target}...")

def banner_grab(target, port):
    print(f"{INFO} starting banner grab on {target} via port {port}...")

def dns_lookup(target):
    print(f"{INFO} starting DNS lookup on {target}...")

def usage():
    print("Usage:")
    print(f"  python3 molecule.py arp-scan <IP/CIDR>")
    print(f"  python3 molecule.py port-scan <IP>")
    print(f"  python3 molecule.py banner-grab <IP> <port>")
    print(f"  python3 molecule.py dns-lookup <hostname>")
    sys.exit(1)

if __name__ == "__main__":
    banner()

    # user did not provide enough arguments - COME ON MAN 
    if len(sys.argv) < 3:
        usage()

    command = sys.argv[1]
    target = sys.argv[2]

    if command == "arp-scan":
        arp_scan(target)
    elif command == "port-scan":
        port_scan(target)
    elif command == "banner-grab":
            if len(sys.argv) < 4:
                print(f"{BAD} Please provide a port for banner grabbing")
                usage()
            port = int(sys.argv[3])
            banner_grab(target, port)
    elif command == "dns-lookup":
        dns_lookup(target)
