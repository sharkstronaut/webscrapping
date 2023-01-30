'''
(1) First try at a Nike.com scrapper.
'''

import requests                
from bs4 import BeautifulSoup  

def search_Nike(query):

    sneakers = []

    productname = []
    retailprice = []

    # Make GET request to site
    url = 'https://www.nike.com/gb/w?q={query}&vst={query}'
    html = requests.get(url)
    
    # Using html parser instead of lxml for easier methods in this webpage
    soup = BeautifulSoup(html.text, 'html.parser')

    # Find all product elements
    products = soup.find_all('div', {'class': 'product-card__body'})

    # Loop through product elements and print name
    for product in products:
        productname.append((product.find('a', {'class': 'product-card__link-overlay'}).text))
        retailprice.append((product.find('div', {'class': 'product-card__price'}).text))
    
    # Make an individual dictionary for each product to add to total product list
    for i in range(len(productname)):
        individual_product = {
            'productName':productname[i],
            'retailPrice':retailprice[i]
        }
        sneakers.append(individual_product)

    # Return list of dictionaries containing all the products and their retail price.
    return sneakers