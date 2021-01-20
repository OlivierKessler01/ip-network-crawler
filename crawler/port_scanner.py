import nmap3
import timeit
import json
import sys

class PortScanner:
    '''
        Allows you to scan for ports opened
    '''
    
    def scan_for_ports_opened(self, domain_or_ip, number_ports=10) -> str:
        '''
         Uses python-nmap to scan for the top 10 most common ports in search for opened ones
        '''
        nmap = nmap3.Nmap()
        #result = nmap.scan_top_ports(domain_or_ip, number_ports)
        #nmap arguments : 
        #       -f : Fragment TCP packets to make it harder for firewalls to detect the sniffing
        #      -Pn : No ping, disables host discovery, scans everything
        # --badsum : Asks nmap to use an
        #invalid checksum, any firewall answering the request doesn't bother checking checksum
        #   --open : Show only open ports
        result = nmap.scan_top_ports(domain_or_ip, number_ports, args=" -f --open")
        return result

    def scan_domain(self, domain_or_ip : str):
        start = timeit.default_timer()
        result = self.scan_for_ports_opened(domain_or_ip, 20)
        print("The result of the scan uses " , sys.getsizeof(str(result))," bytes of memory")
        
        with open('scan.json', "w") as f:
            f.write(json.dumps(result, separators=(',', ':')))
        
        print("Printed result in scan.json")
        stop = timeit.default_timer()
        print ('Time :', stop - start, ' seconds')


