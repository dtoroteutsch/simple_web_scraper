# coding: utf-8
import os
from bs4 import BeautifulSoup

URL = 'http://econpy.pythonanywhere.com/ex/001.html'

def get_page_content(URL):
    print('Starting request to obtain page content...')
    response = requests.get(URL)
    if response.status_code == 200:
        content = response.text
        with open('data/econpy.html', 'w+') as file:
            print('--> Creating file: data/econpy.html')
            file.write(content)

def read_file():
    print('Reading the file...')
    with open('data/econpy.html', 'r') as file:
        content = file.read()
        soup = BeautifulSoup(content, 'html.parser')
        return soup

def get_page_title(soup):
    print('---> Getting Page Title...')
    page_title = soup.find('title')
    print(page_title.text)

def get_items_by_tags(soup):
    print('----> Getting the Item List and Prices by HTML tags...')
    for element in soup.find_all('div', {'title': 'buyer-info'}):
        item_name = element.find('div')
        item_price = element.find('span')
        print(f'{item_name.text}: {item_price.text}')

def get_items_by_child_attribute(soup):
    print('----> Getting the Item List and Prices by child attributes...')
    for element in soup.find_all('div', {'title': 'buyer-info'}):
        item_name = element.div.text
        item_price = element.span.text
        print(f'{item_name}: {item_price}')

def get_item_prices_by_css_attributes(soup):
    print('----> Getting the Item List and Prices by css attributes...')
    #for element in soup.find_all(attrs = {'class': 'item-price'}):
    for element in soup.find_all(class_ = 'item-price'):
        if element.name == 'span':
            print(element.text)

def get_item_price_by_name(soup, item_name = ''):
    print(f'----> Getting price for the item {item_name}...')
    item_price = soup.find('div', string = item_name).next_sibling.next_sibling
    print('Item: {} - Price: {}'.format(item_name, item_price.text))
    

if __name__ == '__main__':
    if 'econpy.html' not in os.listdir('./data/'):
        get_page_content(URL)
    soup = read_file()
    get_item_price_by_name(soup, 'Carson Busses')
        


