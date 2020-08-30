# coding: utf-8
import requests
import os
from bs4 import BeautifulSoup

BASE_URL = 'https://pokemondb.net'

def get_page_content(url, save_file = False, file_name = ''):
    print('Starting request to obtain page content...')
    response = requests.get(url)
    if response.status_code == 200:
        content = response.text
        if save_file:
            with open(file_name, 'w+') as file:
                print(f'--> Creating file: {file_name}')
                file.write(content)
                return
        return content

def read_file():
    print('Reading the file...')
    with open('data/pokedex.html', 'r') as file:
        content = file.read()
        soup = BeautifulSoup(content, 'html.parser')
        return soup

def get_pokedex(soup):
    print('---> Getting Pokedex...')
    pokedex = soup.find('table', {'id': 'pokedex'})
    return pokedex

def get_all_pokemon(pokedex):
    print('----> Getting all pokemon...')
    for row in pokedex.tbody.find_all('tr'):
        pokemon_name = row.find(class_ = 'cell-name').a
        pokemon_types = row.find(class_ = 'cell-icon').find_all('a')
        pokemon_types = [type.text for type in pokemon_types]
        pokemon_species = get_pokemon_data(pokemon_name).find('tr', string = 'Species').next_sibling.next_sibling 
        print(f'{pokemon_name.text}: {pokemon_types} - {pokemon_species}')

def get_pokemon_data(pokemon_name):
    print(f'-----> Getting {pokemon_name.text} data...')
    pokemon_content = get_page_content(f"{BASE_URL}{pokemon_name.get('href')}")
    soup = BeautifulSoup(pokemon_content, 'html.parser')
    pokemon_data = soup.find('h2', string = 'Pokédex data').parent
    return pokemon_data.tbody

def get_pokemon_by_name(pokedex, pokemon_name = ''):
    print('----> Getting {} data...'.format(pokemon_name))
    pokemon = pokedex.find('a', string = pokemon_name).parent.parent
    pokemon_name = pokemon.find(class_ = 'cell-name').a
    pokemon_types = pokemon.find(class_ = 'cell-icon').find_all('a')
    pokemon_types = [type.text for type in pokemon_types]
    pokemon_species = get_pokemon_data(pokemon_name).find('th', string = 'Species').next_sibling.next_sibling
    
    print(f'{pokemon_name.text}: {pokemon_types} - {pokemon_species.text}')

if __name__ == '__main__':
    URL = f'{BASE_URL}/pokedex/all'
    if 'pokedex.html' not in os.listdir('./data/'):
        get_page_content(URL, True, 'data/pokedex.html')
    soup = read_file()
    if soup:
        pokedex = get_pokedex(soup)
        get_pokemon_by_name(pokedex, 'Bulbasaur')

