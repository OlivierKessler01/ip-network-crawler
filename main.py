from crawler.crawler import CrawlerFactory
from crawler.port_scanner import PortScanner
import sys, getopt

def main(argv): 
    try:
        if argv[0] == "scan_ports":
            domains = [argv[1]]
            port_scanner = PortScanner()
            port_scanner.scan_domain(domains[0])
        elif argv[0] == "crawl":
            crawler_factory = CrawlerFactory()
            crawler = crawler_factory.get('ssh')
            crawler.crawl_file()
        else:
            raise IndexError
    except IndexError:
        print('#Scanning network')
        print('Only two way of using it this app :')
        print('sudo python3 main.py scan_ports XXX.XXX.XXX.XXX/XX, CIDR notation for a range of IP')
        print('sudo python3 main.py scan_ports XXX.XXX.XXX.XXX, for a single IP')
        print('sudo python3 main.py scan_ports domain.domain')
        print('#Seeking unprotected servers')
        print('sudo python3 main.py crawl')
       
if __name__ == "__main__":
    main(sys.argv[1:])

