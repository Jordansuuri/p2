from bs4 import BeautifulSoup
import requests
import csv


# Créer une variable où on rentre l'url qui va nous servir à l'inclure dans la fonction request #

url = 'http://books.toscrape.com/catalogue/category/books/nonfiction_13/index.html'


# Créer une variable où on utilise l'url avec la methode "get" du module Request. Si on a une bonne reponse (200): on peut demander la suite #
response = requests.get(url)

# Boucle if : si la reponse est bien 200, on peut demander les informations #
if response.ok:
# recupération du contenu de l'url en brut #
    content = response.content
# Variable parser qui utiliser BS #
    soup = BeautifulSoup(content, "html.parser")


# nombre de livre à extraire sur la page
url_len = len(soup.select("h3"))
url_page = []
indice_livre = 0
#Recupération d'un seul livre, position 4, indice 3
for loop in range(url_len):
    url_len = len(soup.select("h3"))
    url_product_h3 = soup.select("h3")
    url_product_href = url_product_h3[indice_livre].find("a")
    url_product = url_product_href['href'].replace('../../..','http://books.toscrape.com/catalogue')
    print("voici les pages ajoutés : "+url_product)
    url_page.append(url_product)
    indice_livre += 1





