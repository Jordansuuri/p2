from bs4 import BeautifulSoup
import requests
import csv

# reminder des variables demandées (dans l'ordre):

# product_page_url
# universal_product_code
# title
# price_including_tax
# price_excluding_tax
# number_available
# product_description
# category
# review_rating
# image_url

# Créer une variable où on rentre l'url qui va nous servir à l'inclure dans la fonction request #
def page_scrap():
    url = 'http://books.toscrape.com/catalogue/1000-places-to-see-before-you-die_1/index.html'

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

    print(info)
    # ajout separateur ; dans le tableau info
    ligne_csv = ";".join(info)

    #On definit les differentes categories dans le csv & on ecris les differentes variables dans le csv


    with open('info_site.csv', "w+") as file:
        file.write("universal_product_code;title;price_including_tax;price_excluding_tax;number_available;product_description;category;review_rating;image_url\n")
        file.write(universal_product_code + ';')
        file.write(title + ';')
        file.write(price_including_tax+ ';')
        file.write(price_excluding_tax+ ';')
        file.write(number_available+ ';')
        file.write(product_description + ';')
        file.write(category+ ';')
        file.write(review_rating+ ';')
        file.write(image_url+ ';')


    # Manque toujours : product_page_url
page_scrap()
