from bs4 import BeautifulSoup
import requests
import csv
import time


url_category = 'http://books.toscrape.com/catalogue/category/books/fiction_10/index.html'
response = requests.get(url_category)

with open('info_site.csv', "a+") as file:
    file.write("universal_product_code;title;price_including_tax;price_excluding_tax;number_available;product_description;category;review_rating;image_url\n")

content = response.content
soup = BeautifulSoup(content, "html.parser")
def page_scrap(url_product):
    url = url_product
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

    #image_url, recupéra via la balise img, puis chercher dans le dictionnaire rsc
        img_balise = soup.find('img')
        image_url = img_balise['src'].replace('../..','http://books.toscrape.com')

    # Ajoute les variable vers la liste info #
    info = []
    info.append(universal_product_code)
    info.append(title)
    info.append(price_including_tax)
    info.append(price_excluding_tax)
    info.append(number_available)
    info.append(product_description)
    info.append(review_rating)
    info.append(category)
    info.append(image_url)

    # ajout separateur ; dans le tableau info
    ligne_csv = ";".join(info)

    #On definit les differentes categories dans le csv & on ecris les differentes variables dans le csv

    with open('info_site.csv', "a+") as file:
        file.write(universal_product_code + ';')
        file.write(title + ';')
        file.write(price_including_tax+ ';')
        file.write(price_excluding_tax+ ';')
        file.write(number_available+ ';')
        file.write(product_description + ';')
        file.write(category+ ';')
        file.write(review_rating+ ';')
        file.write(image_url+ ';\n')


url_len = len(soup.select("h3"))
url_page = []
indice_livre = 0
for loop in range(url_len):
    url_len = len(soup.select("h3"))
    url_product_h3 = soup.select("h3")
    url_product_href = url_product_h3[indice_livre].find("a")
    url_product = url_product_href['href'].replace('../../..','http://books.toscrape.com/catalogue')
    url_page.append(url_product)
    indice_livre += 1
    print("voici les pages ajoutés : " + url_product)
    page_scrap(url_product)




