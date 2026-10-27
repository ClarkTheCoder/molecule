# molecule
network recon tool by naughty_b0y

## Usage
python3 molecule.py arp-scan <IP/CIDR>
python3 molecule.py arp-scan auto
python3 molecule.py port-scan <IP>
python3 molecule.py port-scan <IP> <timeout>
python3 molecule.py banner-grab <IP> <port>
python3 molecule.py dns-lookup <hostname>

## Features
- ARP scanner -- discover live hosts on local network (supports auto subnet detection)
- Port scanner -- sweep common ports on a target IP (configurable timeout, default 1s)
- Banner grabber -- grab service banners from open ports (coming soon)
- DNS lookup -- resolve hostnames and reverse lookup IPs (coming soon)

## Examples
python3 molecule.py arp-scan auto
python3 molecule.py arp-scan 192.168.1.0/24 2
python3 molecule.py port-scan 192.168.1.1
python3 molecule.py port-scan 192.168.1.1 3