from crawler.crawler import CrawlerInterface
from crawler.port_tester import PortTester

def main(): 
    domains = [("handicap-international.org",), ("olivier-wandering.blog",)]
    port_tester = PortTester()
    port_tester.scan_domains_multithreaded(domains=domains)
       
if __name__ == "__main__":
    main()

