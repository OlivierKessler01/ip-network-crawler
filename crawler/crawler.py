from design_patterns.factory import Factory

'''
Class that crawls the ipv4 network in research for open files
'''
class CrawlerInterface:
    ports = []

    def crawl(self) -> str:
        pass

class CrawlerSMB(CrawlerInterface):
    def crawl(self) -> str:
        return "Done"
    ports = []

class CrawlerMysql(CrawlerInterface):
    def crawl(self) -> str:
        return "Done"
    ports = ['3306']

class CrawlerRsync(CrawlerInterface):
    def crawl(self) -> str:
        return "Done"
    ports = []

class CrawlerFactory:
    classes_to_instanciate = {
        'smb' : CrawlerSMB,
        'rsync' : CrawlerRsync,
        'mysql' : CrawlerMysql 
    }

    def __init__(self, classes_to_instanciate: dict[str, str]):
        self.generic_factory = Factory(classes_to_instanciate)




    
       
    
