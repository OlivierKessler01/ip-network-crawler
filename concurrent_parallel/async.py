import asyncio
import timeit
import urllib.parse
import functools

async def http_get_site(url):
    url = urllib.parse.urlsplit(url)

    reader, writer = await asyncio.open_connection(
        url.hostname,
        80
    )

    request = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % url.hostname
    print('Request : ' + request)
    writer.write(request.encode())
    await writer.drain()

    data = await reader.read(20000)
    print('\n')
    print('Received: ' + data.decode().rstrip())
    print("Close the connection")
    
    writer.close()
    await writer.wait_closed()

   
async def download_all_sites(sites):
    tasks = []

    for url in sites:
        task = asyncio.ensure_future(http_get_site(url))
        tasks.append(task)
    await asyncio.gather(*tasks, return_exceptions=True)

             
if __name__ == "__main__":
    sites = [
        "http://stephanemourey.fr",
        "http://olivier-wandering.blog"
    ]
    

    asyncio.get_event_loop().run_until_complete(download_all_sites(sites))