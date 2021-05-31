from bs4 import BeautifulSoup
import requests
import csv
from time import time

url = 'http://books.toscrape.com/index.html'


response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, "html.parser")



category_list = []
category_links = []
category_names = []
for category_text in soup.find_all('a'):
    category_list.append(category_text.get('href'))
del category_list[0:3]
del category_list[51:-1]
del category_list[-2:-1]
del category_list[-1]

# recuperer les liens et traiter chaque elements de la liste pour ajouter la racine
for lien_category in category_list:
    link = "http://books.toscrape.com/"+ lien_category
    category_links.append(link)


#récupération des nom de catégories à partir des liens extraits (convertir en STR, pour chaque lien : split & recuperer la bonne partie
for category_name in category_list:
    category_name = str(category_name)
    category_name_final = category_name.split('catalogue/category/books/')
    category_name_final2 = category_name_final[1].split('/index.html')
    category_name_final3 = category_name_final2[0].split('_')
    category_names.append(category_name_final3[0])
    print(category_name)

print(category_names)