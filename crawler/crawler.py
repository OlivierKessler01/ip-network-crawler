from design_patterns.factory import Factory

'''
Class that crawls the ipv4 network in research for open files
'''
class Crawler:
    ports = []    

class CrawlerSMB(Crawler):
    ports = []

class CrawlerMysql(Crawler):
    ports = ['3306']

class CrawlerRsync(Crawler):
    ports = []

class CrawlerFactory:
    classes_to_instanciate = {
        'smb' : CrawlerSMB,
        'rsync' : CrawlerRsync,
        'mysql' : CrawlerMysql 
    }

    def __init__(self, classes_to_instanciate: dict[str, str]):
        self.generic_factory = Factory(classes_to_instanciate)




    
       
    
