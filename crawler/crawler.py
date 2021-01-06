import uuid

from smbprotocol.connection import Connection, Dialects
import nmap3

'''
Class that crawls the ipv4 network in research for open files
'''
class Crawler:
    smb_ports = []
    rsync_ports = []
    mysql_ports = []

    def scan_for_ports_opened(self, protocol) -> int:

        nmap = nmap3.Nmap()
        result = nmap.scan_top_ports("scanme.nmap.org")
        print(type(result))
        print(result)
        return 0
    
       
    
