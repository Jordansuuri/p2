# Programme Projet 2 OpenClassrooms : webscrapping.

__Bonjour, je vous présente le programme permettant de scrap le site web : books.toscrape.com__

## Mise en place de l'environnement virtuel necessaire au programme :

# Voici les différentes commandes à utiliser afin d'installer dans l'environnement virtuel les différents packages.

* `pip install beautifulsoup4`
* `pip install requests`


## Le programme s'articule en 3 éléments distinctes.

## Scrap_from_book.py :

Ce dernier scrap uniquement 1 page choisis arbitrairement par l'utilisateur.
La commande afin de scraper une page du site http://books.toscrape.com/index.html
est la suivante :
* `page_scrap("url de la page","nom du livre")`

*Ainsi le fichier csv & l'image du bouquin seront respectivement dans le dossier "csv" et "images"*

## Scrap_from_category.py :

A la même manière de "Scrap_from_book.py", ce dernier permet de scraper une catégorie entière.
Il faudra donc utiliser la fonction : 
* `scrap_category("url de la categorie","nom du livre")`

*Le comportement en matière d'extraction de csv & de telechargement d'images est similaire a celui de Scrap_from_book.py.*

## Scrap_from_index.py :

Le fonctionnement est ici différent, il suffit simplement de lancer l'application pour scrap le site en entier directement.
L'url est déjà renseigné, tout va donc se scrap automatiquement. Il procede donc catégorie par catégorie.

*Le comportement en matière d'extraction de csv & de telechargement d'images est similaire a celui de Scrap_from_book.py.*
