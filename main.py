from crawler.crawler import CrawlerFactory
import sys, getopt

def main(argv): 
    try:
        if argv[0] == "scan_port":
            domains = ["178.79.146.0/26"]
            port_scanner = PortScanner()
            port_scanner.scan_domain(domains[0])
        elif argv[0] == "crawl":
            crawler_factory = CrawlerFactory()
            crawler = crawler_factory.get('ssh')
            crawler.crawl(['google.fr'])
        else:
            raise IndexError
    except IndexError:
        print('Only two way of using it this app :')
        print('sudo python3 main.py scan_port')
        print('sudo python3 main.py crawl')
       
if __name__ == "__main__":
    main(sys.argv[1:])

