from bs4 import BeautifulSoup
import requests
import csv
from time import time


# CHANGER LE NOM DU FICHIER CSV PAR LE NOM DE LA CATEGORIE => with open (nom_variable_category, 'w')
def mk_csv():
    with open('info_site.csv', "w") as file:
        file.write("product_page_url;universal_product_code;title;price_including_tax;price_excluding_tax;number_available;product_description;category;review_rating;image_url\n")

url_category = 'http://books.toscrape.com/catalogue/category/books/childrens_11/index.html'
response = requests.get(url_category)
content = response.content
soup = BeautifulSoup(content, "html.parser")

def page_scrap(product_page_url):
    url = product_page_url
     # Créer une variable où on utilise l'url avec la methode "get" du module Request. Si on a une bonne reponse (200): on peut demander la suite #
    response = requests.get(url)
    # Boucle if : si la reponse est bien 200, on peut demander les informations #
    if response.ok:
    # recupération du contenu de l'url en brut #
        content = response.content
    # Variable parser qui utiliser BS #
        soup = BeautifulSoup(content, "html.parser")
    # Récupération des td #
        td_informations = soup.find_all("td")
    # universal_product_code
        universal_product_code = td_informations[0].text
    # product_description
        product_description = soup.find_all('p')[3].text.replace(';',',')
    # price_excluding_tax
        price_excluding_tax = td_informations[2].text.replace('£','')
    # price_including_tax
        price_including_tax = td_informations[3].text.replace('£','')
    # number_available
        number_available = td_informations[5].text.replace('In stock (','').replace(' available)', '')
    # review_rating
        review_rating = td_informations[6].text
    # recuperer le titre du livre et le met dans une liste via find_all#
        titre_balise = soup.find_all("h1")
    # title
        title = titre_balise[0].text
    # Category
        category = soup.find(class_="breadcrumb").text.split('\n')[-4]
    #image_url, recupéra via la balise img, puis chercher dans le dictionnaire src
        img_balise = soup.find('img')
        image_url = img_balise['src'].replace('../..','http://books.toscrape.com')
    # On definit les differentes categories dans le csv & on ecris les differentes variables dans le csv
    with open('info_site.csv', "a+") as file:
        file.write(product_page_url + ';')
        file.write(universal_product_code + ';')
        file.write(title + ';')
        file.write(price_including_tax + ';')
        file.write(price_excluding_tax + ';')
        file.write(number_available + ';')
        file.write(product_description + ';')
        file.write(category + ';')
        file.write(review_rating + ';')
        file.write(image_url + ';\n')
        file.close



# création d'une condition si le bouton next existe : on créer une nouvelle url (next_url)
next_exist = soup.find_all(class_="next")
url_len = len(soup.select("h3"))
url_page = []
indice_livre = 0


for loop in range(url_len):
    url_product_h3 = soup.select("h3")
    url_product_href = url_product_h3[indice_livre].find("a")
    product_page_url = url_product_href['href'].replace('../../..','http://books.toscrape.com/catalogue')
    url_page.append(product_page_url)
    indice_livre += 1
    page_scrap(product_page_url)
    print("voici les pages ajoutés : " + product_page_url)

if len(next_exist) > 0:
    next_balise = str(next_exist[0]).split('">')
    next_split = next_balise[1].split('"')
    next_url = next_split[1]
    next_balise = url_category.split('/')
    next_balise[-1] = next_url
    next_url = '/'.join(next_balise)
    url_category = next_url
    print(url_category)
    # PB => CA SCRAP LA DERNIERE PAGE
    page_scrap(product_page_url)


print(product_page_url)