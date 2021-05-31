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
del category_list[-1]

# recuperer les liens et traiter chaque elements de la liste pour ajouter la racine
for lien_category in category_list:
    link = "http://books.toscrape.com/"+ lien_category
    category_links.append(link)

print(category_links)

