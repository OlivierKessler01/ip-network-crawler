from design_patterns.factory import Factory
from paramiko import AutoAddPolicy, SSHClient, SSHException, AuthenticationException
from socket import error

'''
Classes that tests servers in search for non-protected services
'''
class CrawlerInterface:
    def __init__(self):
        self.ports = []

    def crawl(self, domains: list) -> str:
        pass

class CrawlerSMB(CrawlerInterface):
    def __init__(self):
        self.ports = []

    def crawl(self, domains : list) -> str:
        return "Done"

class CrawlerMysql(CrawlerInterface):
    def __init__(self):
        self.ports = ['3306']

    def crawl(self, domains : list) -> str:
        return "Done"

class CrawlerRsync(CrawlerInterface):
    def __init__(self):
        self.ports = []

    def crawl(self, domains : list) -> str:
        return "Done"

class CrawlerSsh(CrawlerInterface):
    def __init__(self):
        self.ports = ['22']

    def crawl(self, domains : list) -> str:
        for domain in domains:
            try:
                print('Trying SSH connect to ', domain)
                client = SSHClient()
                client.set_missing_host_key_policy(AutoAddPolicy)
                client.connect(domain, port=self.ports[0], username="root", password="root", look_for_keys=False, allow_agent=False)
                print("SSH server not protected : ", domain)
                client.close()
            except SSHException as err:
                print('SSHException : ', str(err))
                continue
            except AuthenticationException as err:
                print('AuthenticationException : ', str(err))
                continue
            except error as err:
                print('Socket.error : ', str(err))
                continue

            print('Done trying SSH connection to domains')

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


    
       
    
