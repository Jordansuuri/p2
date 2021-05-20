from bs4 import BeautifulSoup
import requests
import lxml

# reminder des variables demandées:
# title
# universal_product_code
# price_including_tax
# price_excluding_tax
# number_available
# product_description
# category
# review_rating

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
# Récupération des td #
    td_informations = parser.find_all("td")
# universal_product_code
    universal_product_code = td_informations[0].text
# product_description
    product_description = td_informations[1].text
# price_including_tax
    price_including_tax = td_informations[2].text
# price_excluding_tax
    price_excluding_tax = td_informations[3].text
# number_available
    number_available = td_informations[5].text
# review_rating
    review_rating = td_informations[6].text
# recuperer le titre du livre et le met dans une liste via find_all#
    titre_balise = parser.find_all("h1")
# title
    title = titre_balise[0].text
# review_rating

    print(td_informations)
    print(universal_product_code)
    print(title)
    print(product_description)
    print(price_including_tax)
    print(price_excluding_tax)
    print(number_available)
    print(review_rating)



