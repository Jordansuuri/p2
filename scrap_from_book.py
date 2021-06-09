from bs4 import BeautifulSoup
import requests



def page_scrap(product_page_url,nom):
     # Créer une variable où on utilise l'url avec la methode "get" du module Request. Si on a une bonne reponse (200): on peut demander la suite #
    response = requests.get(product_page_url)
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
    # .replace des point virgules dans la description par des simples virgules
        product_description = soup.find_all('p')[3].text.replace(';',',')
        if product_description == '' :
            product_description = "pas de description"
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
        dwn_image(image_url)
  # On definit les differentes categories dans le csv & on ecris les differentes variables dans le csv
    with open("csv/"+nom+'.csv', "a+", encoding="utf-8") as file:
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

#Extraction des images dans un dossier images
def dwn_image(url):
    res = requests.get(url)
    n = url.split('/')
    fichier = open("images/"+ n[-1], "wb")
    fichier.write(res.content)
    fichier.close()

page_scrap("http://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html","tipping the velvet")