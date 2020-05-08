### Nadia Uddin
### 08/05/2020

import random2

import requests

def random_pokemon():
    """Creating a Pokemon top trumps game"""
    pokemon_id = random2.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}'.format(pokemon_id)

    response = requests.get(url)
    pokemon = response.json()
