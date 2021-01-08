import nmap3

class PortTester:
    def scan_for_ports_opened(self, domain_or_ip, number_ports=10) -> str:
        '''
         Uses python-nmap to scan for the top 10 most common ports in search for opened ones
        '''
        nmap = nmap3.Nmap()
        result = nmap.scan_top_ports(domain_or_ip, number_ports, args="-f --badsum -Pn")
        return result