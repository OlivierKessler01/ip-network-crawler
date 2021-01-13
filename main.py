from crawler.crawler import CrawlerInterface
from crawler.port_tester import PortTester

def main(): 
    domains = ["178.79.146.0/26"]
    port_tester = PortTester()
    #port_tester.scan_domains_multithreaded(domains=domains)
    port_tester.scan_domain(domains[0])
       
if __name__ == "__main__":
    main()

