# Create virtualenv
```sh
python3 -m venv env
source env/bin/activate
sudo pip install -r requirements.txt
```

# Usage
```sh
# Sniff ports using nmap and dump result in a file
sudo python3 main.py scan_ports XXX.XXX.XXX.XXX/XX # CIDR notation for a range of IPs
sudo python3 main.py scan_ports XXX.XXX.XXX.XXX # for a single IP
sudo python3 main.py scan_ports domain.domain
# Using the previously dumped file, try to connect to the hosts using multiple protocols
sudo python3 main.py crawl
```
