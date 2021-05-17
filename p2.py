from bs4 import Beautifulsoup
import requests

url = 'http://books.toscrape.com/index.html'

response = requests.get(url)

if response.ok:
    soup = Beautifulsoup(response.text)
    print(soup)
