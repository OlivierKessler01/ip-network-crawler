from design_patterns.factory import Factory
from paramiko import AutoAddPolicy, SSHClient, SSHException, AuthenticationException
from socket import error
import json
from os import chmod

'''
Classes that tests servers in search for non-protected services
'''
class CrawlerInterface:
    def __init__(self):
        self.ports = []
        self.dictionary_credentials = [
            ['root', 'root'],
            ['admin', 'admin'],
            ['root' , 'admin'],
            ['admin', 'root'],
            ['root', '123'],
            ['user' , 'user'],
            ['test', 'test'],
            ['ubuntu', 'ubuntu'],
            ['oracle', 'oracle']
        ]
    
    def crawl_file(self, filename="scan.json") -> str:
        pass

class CrawlerSMB(CrawlerInterface):
    def __init__(self):
        super().__init__()
        self.ports = []

    def crawl_file(self, filename="scan.json") -> str:
        return "Done"

class CrawlerMysql(CrawlerInterface):
    def __init__(self):
        super().__init__()
        self.ports = ['3306']

    def crawl_file(self, filename="scan.json") -> str:
        return "Done"

class CrawlerRsync(CrawlerInterface):
    def __init__(self):
        super().__init__()
        self.ports = []

    def crawl_file(self, filename="scan.json") -> str:
        return "Done"

class CrawlerSsh(CrawlerInterface):
    def __init__(self):
        super().__init__()
        self.ports = ['22']
        
    def try_to_connect(self, host):
        '''
            Iterate throuh the credentials dictionnary and try to connect
        '''
        for credential in self.dictionary_credentials:
            try:
                print(
                    'Trying SSH connect to ', 
                    host, 'with : ', credential[0], ':', credential[1]
                )
                client = SSHClient()
                client.set_missing_host_key_policy(AutoAddPolicy)
                client.connect(
                    host, 
                    timeout=2, 
                    port=self.ports[0], 
                    username=credential[0], 
                    password=credential[1], 
                    look_for_keys=False, 
                    allow_agent=False
                )
                print("SSH server not protected : ", host)
                with open("unprotected_hosts_ssh.txt", "a") as f:
                    f.write(str(host) + "\n")
                break

            except AuthenticationException as err:
                with open("authentication_error_ssh.txt", "a") as f:
                    f.write(str(host) + "\n")
                print('AuthenticationException : ', str(err))
            except SSHException as err:
                print('SSHException : ', str(err))
                break;
            except error as err:
                print('Socket.error : ', str(err))
            
            client.close()


    def crawl_file(self, filename="scan.json") -> str:
        '''
            Parses the json file containing the nmap result
            Then calls the function which tries to connect
        '''
        with open(filename, "r") as json_data:
            data = json.load(json_data)

        #Empty results file
        with open("unprotected_hosts_ssh.txt", "w") as f:
            f.truncate(0)

        with open("authentication_error_ssh.txt", "w") as f:
            f.truncate(0)

        chmod("unprotected_hosts_ssh.txt", 0o775)
        chmod("authentication_error_ssh.txt", 0o775)
           
        for d in data.items():
            try:
                for port in d[1]['ports']:
                    if (port['protocol'] == "tcp" and
                        port["portid"] == self.ports[0] and 
                        port['state'] == "open"):
                        self.try_to_connect(d[0])
                        print('Done trying SSH connection to :', d[0])
            except KeyError:
                continue
            except IndexError as err:
                continue

class CrawlerFactory:
    def __init__(self):
        classes_to_instanciate = {
            'smb' : CrawlerSMB,
            'rsync' : CrawlerRsync,
            'mysql' : CrawlerMysql,
            'ssh' : CrawlerSsh
        }

        self.generic_factory = Factory(classes_to_instanciate)

    def get(self, service):
        return self.generic_factory.get(service)


    
       
    
