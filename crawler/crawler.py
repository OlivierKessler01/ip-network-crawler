from design_patterns.factory import Factory
from paramiko import AutoAddPolicy, SSHClient, SSHException, AuthenticationException
from socket import error
import json

'''
Classes that tests servers in search for non-protected services
'''
class CrawlerInterface:
    def __init__(self):
        self.ports = []

    def crawl_file(self, filename="scan.json") -> str:
        pass

class CrawlerSMB(CrawlerInterface):
    def __init__(self):
        self.ports = []

    def crawl_file(self, filename="scan.json") -> str:
        return "Done"

class CrawlerMysql(CrawlerInterface):
    def __init__(self):
        self.ports = ['3306']

    def crawl_file(self, filename="scan.json") -> str:
        return "Done"

class CrawlerRsync(CrawlerInterface):
    def __init__(self):
        self.ports = []

    def crawl_file(self, filename="scan.json") -> str:
        return "Done"

class CrawlerSsh(CrawlerInterface):
    def __init__(self):
        self.ports = ['22']

    def crawl_file(self, filename="scan.json") -> str:
        with open(filename, "r") as json_data:
            data = json.load(json_data)
           
        for d in data.items():
            try:
                for port in d[1]['ports']:
                    if port['protocol'] == "tcp" and port["portid"] == self.ports[0] and port['state'] == "open":
                        try:
                            print('Trying SSH connect to ', d[0])
                            client = SSHClient()
                            client.set_missing_host_key_policy(AutoAddPolicy)
                            client.connect(d[0], timeout=2, port=self.ports[0], username="root", password="v6NMrF25y@", look_for_keys=False, allow_agent=False)
                            print("SSH server not protected : ", d[0])
                            with open("unprotected_hosts_ssh.txt", "w") as f:
                                f.write(str(d[0]) + "\n")

                        except AuthenticationException as err:
                            print('AuthenticationException : ', str(err))
                        except SSHException as err:
                            print('SSHException : ', str(err))
                        except error as err:
                            print('Socket.error : ', str(err))

                        client.close()
                        print('Done trying SSH connection to :', d[0])
            except KeyError:
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


    
       
    
