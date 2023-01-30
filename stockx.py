import requests
import re, json
from bs4 import BeautifulSoup


# Function to print json data in a legible way
def printJSON(r):
    parsed = json.loads(r)
    print(json.dumps(parsed, indent = 4, sort_keys=False))

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

def search_firstProduct(query):
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



'''
(3) Generalized method to find all the products that meet a certain criteria. Returns a dictionary.
'''

def search_allProducts(query):
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
    return output['Products']

'''
(4) Parse thru all products asked by the query and return relevant data, in this case:
    - Cathegory
    - Name
    - Colorway
    - Release date
    - Retail price
    - Highest bid for the product
'''
def get_productData(products):
    sneaker_list = []
    for e in products:
        data = {
            'category':e['category'],
            'name':e['title'],
            'colorway':e['colorway'],
            'releaseDate':e['releaseDate'],
            'retailPrice':e['retailPrice'],
            'highestBid':e['market']['highestBid']
        }
        sneaker_list.append(data)

    return sneaker_list