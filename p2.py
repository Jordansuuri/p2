from bs4 import BeautifulSoup
import requests
import lxml

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

url = 'http://books.toscrape.com/catalogue/quarter-life-poetry-poems-for-the-young-broke-and-hangry_727/index.html'

# Créer une variable où on utilise l'url avec la methode "get" du module Request. Si on a une bonne reponse (200): on peut demander la suite #
response = requests.get(url)

# Boucle if : si la reponse est bien 200, on peut demander les informations #
if response.ok:
# recupération du contenu de l'url en brut #
    content = response.content
# Variable parser qui utiliser BS #
    parser = BeautifulSoup(content, "lxml")
# Récupération des td #
    td_informations = parser.find_all("td")
# universal_product_code
    universal_product_code = td_informations[0].text
# product_description #A CHANGER
    product_description = td_informations[1].text
# price_excluding_tax
    price_excluding_tax = td_informations[2].text.replace('£','')
# price_including_tax
    price_including_tax = td_informations[3].text.replace('£','')
# number_available
    number_available = td_informations[5].text.replace('In stock (','').replace(' available)', '')
# review_rating
    review_rating = td_informations[6].text
# recuperer le titre du livre et le met dans une liste via find_all#
    titre_balise = parser.find_all("h1")
# title
    title = titre_balise[0].text
# Category
    category_balise = parser.find(class_="breadcrumb")
    category_balise = category_balise.text.split('\n')
    category = category_balise[-4]
    print(category)



info = []

# Ajoute les variable la liste info #

info.append(universal_product_code)
info.append(title)
info.append(product_description)
info.append(price_including_tax)
info.append(price_excluding_tax)
info.append(number_available)
info.append(review_rating)
info.append(category)
ligne_csv = ";".join(info)

print(info)
