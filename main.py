from crawler.crawler import Crawler
import timeit
import asyncio

def main():
    start = timeit.default_timer()
    crawler = Crawler()
    crawler.scan_for_ports_opened('SMB')
    stop = timeit.default_timer()
    print ('Time :', stop - start, ' seconds')

if __name__ == "__main__":
    main()

