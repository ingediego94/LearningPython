import requests

"""
Listado de todos los codigos de respuesta con request:
    https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status#successful_responses
    (100-199) = Informational responses
    (200-299) = Successful responses
    (300-399) = Redirection messages 
    (400-499) = Client error responses
    (500-599) = Server error responses
"""

url = 'https://pokeapi.co/api/v2/pokemon/'

pokemon = input("Que pokemon desear consultar:  ").lower().strip()

respuesta = requests.get(url + pokemon)

datosJSON = respuesta.json()

print(datosJSON)


#habilidades = datosJSON['moves']

for move in datosJSON['moves']:
    print(move["move"]["name"])
