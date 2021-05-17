from bs4 import BeautifulSoup
import requests

url = 'http://books.toscrape.com/index.html'

response = requests.get(url)

if response.ok:
    soup = BeautifulSoup(response.text)
    print(soup)
