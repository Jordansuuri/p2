from bs4 import BeautifulSoup
import requests
import lxml

# Créer une variable où on rentre l'url qui va nous servir à l'inclure dans la fonction request #

url = 'http://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html'

# Créer une variable où on utilise l'url avec la methode "get" du module Request. Si on a une bonne reponse (200): on peut demander la suite #
response = requests.get(url)

# Boucle if : si la reponse est bien 200, on peut demander les informations #
if response.ok:
    # recupération du contenu de l'url en brut #
    content = response.content
    # Variable parser qui utiliser BS #
    parser = BeautifulSoup(content, "lxml")
    # recuperer le titre du livre et le met dans une liste via find_all#
    titre_balise = parser.find_all("h1")
    titre_livre = titre_balise[0].text
    # Titre recupéré en text
    print(titre_livre)


