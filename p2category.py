from bs4 import BeautifulSoup
import requests
import csv
import time


url_category = 'http://books.toscrape.com/catalogue/category/books/food-and-drink_33/index.html'
response = requests.get(url_category)
if response.ok:
    content = response.content
    soup = BeautifulSoup(content, "html.parser")

# Category
category_on_category = soup.find(class_="breadcrumb").text.split('\n')[-2]


url_len = len(soup.select("h3"))
url_page = []
indice_livre = 0

#SI href_exist => VARIABLE PRESENTE => CONCATENER ET AJOUTER LE page number AU LIEN + SUPPRESSION DERNIER LIEN
#incrementer le numero de page puis l'ajouter a l'url de la categorie si le href est present

page_number = 0
href_exist = soup.find_all(class_="next")
url_nouvelle_page = "http://books.toscrape.com/catalogue/category/books"
#chercher le lien de la page (quand on est sur category
url_category_page = soup.find_all("strong")
print(href_exist)

for loop in range(url_len):
    url_len = len(soup.select("h3"))
    url_product_h3 = soup.select("h3")
    url_product_href = url_product_h3[indice_livre].find("a")
    url_product = url_product_href['href'].replace('../../..', 'http://books.toscrape.com/catalogue')
    url_page.append(url_product)
    indice_livre += 1
    #print("voici les pages ajoutés : " + url_product)

