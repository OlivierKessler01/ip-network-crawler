import nmap3
import timeit
#import asyncio
import threading
import json

class PortTester:
    '''
        Allows you to scan for ports opened, given a domain list, and using multi-threading
        TODO : Test performance using asyncio instead of the threading library
    '''

    def __init__(self):
        self.semaphore = threading.Semaphore()

    def scan_for_ports_opened(self, domain_or_ip, number_ports=10) -> str:
        '''
         Uses python-nmap to scan for the top 10 most common ports in search for opened ones
        '''
        nmap = nmap3.Nmap()
        result = nmap.scan_top_ports(domain_or_ip, number_ports)
        #result = nmap.scan_top_ports(domain_or_ip, number_ports, args="-f --badsum -Pn")
        return result

    def scan_domain(self, domain_or_ip : str):
        self.semaphore.acquire()
        start = timeit.default_timer()
        result = self.scan_for_ports_opened(domain_or_ip, 100)
        print(json.dumps(result, sort_keys=False, indent=4))
        stop = timeit.default_timer()
        print ('Time :', stop - start, ' seconds')
        self.semaphore.release()

    def scan_domains_multithreaded(self, domains:list = []):
        for domain in domains:
            print(domain)
            thread = threading.Thread(target=self.scan_domain, args=domain)  
            thread.start()