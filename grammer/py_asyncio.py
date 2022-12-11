import requests
import asyncio
from bs4 import BeautifulSoup
import time

s = time.time()
results = []
loop = asyncio.get_event_loop()


async def get_page(url):
    req = await loop.run_in_executor(None, requests.get, url)
    html = req.text
    soup = await loop.run_in_executor(None, BeautifulSoup, html, 'lxml')
    return soup


async def main():
    urls = [
        "https://wp.me/p9x2W1-x",
        "https://wp.me/p9x2W1-w",
        "https://wp.me/p9x2W1-t",
        "https://wp.me/p9x2W1-q",
        "https://wp.me/p9x2W1-p",
        "https://wp.me/p9x2W1-j",
        "https://wp.me/p9x2W1-h"
    ]

    fts = [asyncio.ensure_future(get_page(url)) for url in urls]
    r = await asyncio.gather(*fts)                               # using star to disassemble Lists
    global results
    results = r

loop.run_until_complete(main())
loop.close
e = time.time()

print("{0:.2f}초 걸렸습니다.".format(e - s))
