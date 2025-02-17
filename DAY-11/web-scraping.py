"""
    # EXTRAER ELEMENTOS:
        soup.select('div') --> Todos los elementos con la etiqueta 'div'
        soup.select('#estilo_4') --> Elementos que contengan id='estilo4'
        soup.select('.columna_der') --> Elementos que contengan class='columna der'
        soup.select('div span') --> Cualquier elemento llamado 'span' dentro de un elemento 'div'
        soup.select('div>span') --> Cualquier elemento llamado 'span' directamente dentro de un elemento 'div', sin nada en el medio
"""

import bs4
import requests

URL = "https://escueladirecta-blog.blogspot.com/"

resultado = requests.get(URL)
sopa = bs4.BeautifulSoup(resultado.text, "html.parser")

titulo = sopa.select("title")[0].getText()
web_logo = sopa.select("a.header-image-wrapper img")
print(f"Web: {titulo}")
print(f"Logo de la web: {web_logo[0].get('src')}\n")

titulo_de_articulos = sopa.select("div.r-snippetized[class='r-snippetized']")
autor_del_articulo = sopa.select("a[title='author profile']")

for titulo, autor in zip(titulo_de_articulos, autor_del_articulo):
    print(f"\nTitulo de articulo: {titulo.getText().strip()}")
    print(f"Autor del articulo: {autor.getText().strip()}")



