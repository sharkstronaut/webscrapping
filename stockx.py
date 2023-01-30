import requests
import re, json
from bs4 import BeautifulSoup

'''
(1) First try at a search method for sneakers. Returns captcha error.

def search(query):
    url = f'https://stockx.com/api/browse?_search={query}'

    headers = {
        'Accept':'text/html',
        'Accept-Language':'en-US,en;q=0.5',
        'Alt-Used':'stockx.com',
        'Connection':'keep-alive',
        'DNT':'1',
        'Host':'stockx.com',
        'If-None-Match':'W/"10wg4aevn5d4zh5"',
        'Sec-Fetch-Dest':'document',
        'Sec-Fetch-Mode':'navigate',
        'Sec-Fetch-Site':'cross-site',
        'Sec-GPC':'1',
        'TE':'trailers',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/109.0'
    }
    

    html = requests.get(url=url, headers=headers)
    print(html.text)'''

'''
(2) Second try at a search method for sneakers. 
    - Changed the headers to bypass captcha.
    - Returns the first product listed that meets the requirements of the query.
'''

def search_Stockx(query):
    url = f'https://stockx.com/api/browse?_search={query}'

    headers = {
        'accept': 'application/json',
        'accept-encoding': 'utf-8',
        'accept-language': 'en-GB,en;q=0.9',
        'app-platform': 'Iron',
        'referer': 'https://stockx.com/en-gb',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.62 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }

    html = requests.get(url=url, headers=headers)
    output = json.loads(html.text)
    return output['Products'][0]