from crawler.crawler import Crawler
from crawler.port_tester import PortTester
import timeit
#import asyncio
import threading
import json

sem = threading.Semaphore()
start = timeit.default_timer()

def fetch(domain_or_ip : str):
    sem.acquire()
    port_tester = PortTester()
    result = port_tester.scan_for_ports_opened(domain_or_ip, 100)
    print(json.dumps(result, sort_keys=False, indent=4))

    stop = timeit.default_timer()
    print ('Time :', stop - start, ' seconds')
    sem.release()

def main(): 
    domains = [("handicap-international.org",), ("olivier-wandering.blog",)]
    for domain in domains:
        print(domain)
        thread = threading.Thread(target=fetch, args=domain)  
        thread.start()
       
if __name__ == "__main__":
    main()

