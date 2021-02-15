import unittest
from crawler import CrawlerFactory, CrawlerSsh

class CrawlerTest(unittest.TestCase):
    def test_crawler_factory(self):
        factory = CrawlerFactory()
        crawler_ssh = factory.get('ssh')
        self.assertIsInstance(crawler_ssh, CrawlerSsh)

if __name__ == "__main__":
    unittest.main()
