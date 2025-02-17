import bs4
import requests

URL = "https://books.toscrape.com/catalogue/page-{}.html"

for pagina in range(1, 51):
    print(URL.format(pagina))