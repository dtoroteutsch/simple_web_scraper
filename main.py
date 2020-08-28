# coding: utf-8
import requests
import re
import os

URL = 'http://econpy.pythonanywhere.com/ex/001.html'

def get_page_content(URL):
    print('Starting request to obtain page content')
    response = requests.get(URL)
    if response.status_code == 200:
        content = response.text
        with open('data/econpy.html', 'w+') as file:
            print('--> Creating file: data/econpy.html')
            file.write(content)

def read_file():
    print('Reading the file')
    with open('data/econpy.html', 'r') as file:
        content = file.read()
        print('--> Getting the titles')
        regex = '<div title="buyer-name">(.+?)</div>'
        for title in re.findall(regex, content):
            print(title)

if __name__ == '__main__':
    if 'econpy.html' not in os.listdir('./data/'):
        get_page_content(URL)
    read_file()
        


