from stockx import *
from nike_scrapper import *

query = 'Air Jordan'



nike_products = search_Nike(query)

print('Results of your query ', query, 'in the Nike website','\n', nike_products)
print('\n')


print('First result found of your query ', query, 'in the Stockx website (raw data): ','\n', )
first = search_firstProduct(query)
print(first)

print('\n')

products = search_allProducts(query)
relevant_data = get_productData(products)
print('Total results of your query ', query, 'in the Stockx website:','\n', )
for element in relevant_data:
    print(element)
    print('\n')
