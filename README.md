# Create virtualenv
```sh
python3 -m venv env
source env/bin/activate
sudo pip install -r requirements.txt
```

# Usage
```sh
# Only two way of using it this app
sudo python3 main.py scan_ports XXX.XXX.XXX.XXX/XX # CIDR notation for a range of IPs
sudo python3 main.py scan_ports XXX.XXX.XXX.XXX # for a single IP
sudo python3 main.py scan_ports domain.domain
sudo python3 main.py crawl
```
