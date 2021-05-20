from bs4 import BeautifulSoup
import requests
import lxml

# Créer une variable où on rentre l'url qui va nous servir à l'inclure dans la fonction request #

url = 'http://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html'

# Créer une variable où on utilise l'url avec la methode "get" du module Request. Si on a une bonne reponse (200): on peut demander la suite #
response = requests.get(url)

#Boucle if : si la reponse est bien 200, on peut demander les informations#
if response.ok:
    content = response.content
    parser = BeautifulSoup(content, "lxml")
    body = parser.body
    print(body.text)