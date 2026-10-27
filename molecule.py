from scapy.all import ARP, Ether, srp
import sys
import subprocess
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

def get_local_ip():
    result = subprocess.run(["ipconfig", "getifaddr", "en0"], capture_output=True, text=True)
    return result.stdout.strip()

def arp_scan(target):
    if target == "auto":
        local_ip = get_local_ip()
        target = local_ip.rsplit('.', 1)[0] + ".0/24"
        print(f"{INFO} Auto-detected subnet: {target}")

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

def port_scan(target, timeout=1):
    print(f"{INFO} starting port scan on {target}...")
    print(f"{'PORT':<20} {'STATE':20} SERVICE")
    print("-" * 30)

    common_ports = {
        21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP",
        53: "DNS", 69: "TFTP", 80: "HTTP", 110: "POP3",
        111: "RPC", 119: "NNTP", 123: "NTP", 135: "MSRPC",
        137: "NetBIOS", 138: "NetBIOS", 139: "NetBIOS-SSN",
        143: "IMAP", 161: "SNMP", 194: "IRC", 389: "LDAP",
        443: "HTTPS", 445: "SMB", 465: "SMTPS", 500: "IKE",
        512: "rexec", 513: "rlogin", 514: "Syslog", 515: "LPD",
        587: "SMTP-Submit", 631: "IPP", 636: "LDAPS",
        873: "Rsync", 902: "VMware", 993: "IMAPS", 995: "POP3S",
        1080: "SOCKS", 1194: "OpenVPN", 1433: "MSSQL",
        1521: "Oracle", 1723: "PPTP", 2049: "NFS",
        2121: "FTP-Alt", 2375: "Docker", 2376: "Docker-TLS",
        3000: "Dev-Server", 3306: "MySQL", 3389: "RDP",
        4444: "Metasploit", 4500: "IKE-NAT", 5000: "Flask",
        5432: "PostgreSQL", 5900: "VNC", 5985: "WinRM-HTTP",
        5986: "WinRM-HTTPS", 6379: "Redis", 6443: "Kubernetes",
        7001: "WebLogic", 8080: "HTTP-Alt", 8443: "HTTPS-Alt",
        8888: "Jupyter", 9000: "PHP-FPM", 9090: "Prometheus",
        9200: "Elasticsearch", 9300: "Elasticsearch-Cluster",
        27017: "MongoDB", 27018: "MongoDB-Alt"
    }
    open_ports = 0 

    for port, service in common_ports.items():
        print(f"{INFO} Checking port {port}...", end="\r")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((target, port))
        sock.close()

        if result == 0:
            print(f"{port:<20} {'open':<20} {service}")
            open_ports += 1

    print(f"\n{INFO} Port scan complete on {target}. {open_ports} open port(s) found on {target}")

def banner_grab(target, port):
    print(f"{INFO} starting banner grab on {target} via port {port}...")

def dns_lookup(target):
    print(f"{INFO} starting DNS lookup on {target}...")

def usage():
    print("Usage:")
    print(f"  python3 molecule.py arp-scan <IP/CIDR> or auto to auto-detect subnet")
    print(f"  python3 molecule.py port-scan <IP> <timeout> - timeout is set to 1 by default")
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
        timeout = float(sys.argv[3]) if len(sys.argv) > 3 else 1
        port_scan(target, timeout)
    elif command == "banner-grab":
            if len(sys.argv) < 4:
                print(f"{BAD} Please provide a port for banner grabbing")
                usage()
            port = int(sys.argv[3])
            banner_grab(target, port)
    elif command == "dns-lookup":
        dns_lookup(target)
    else:
        print(f"{BAD} Unknown command: {command}")
        usage()