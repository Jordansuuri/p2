from bs4 import BeautifulSoup
import requests
import csv
import time

def test1():
    url_category = 'http://books.toscrape.com/catalogue/category/books/childrens_11/index.html'
    response = requests.get(url_category)
    if response.ok:
        content = response.content
        soup = BeautifulSoup(content, "html.parser")


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