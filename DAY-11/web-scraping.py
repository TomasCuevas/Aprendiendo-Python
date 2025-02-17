import bs4
import requests

URL = "https://escueladirecta-blog.blogspot.com/"

resultado = requests.get(URL)
sopa = bs4.BeautifulSoup(resultado.text, "html.parser")

titulo = sopa.select("title")[0].getText()
print(f"WEB: {titulo}\n")

titulo_de_articulos = sopa.select("div.r-snippetized[class='r-snippetized']")

for titulo in titulo_de_articulos:
    print(f"Titulo de articulo: {titulo.getText().strip()}")
