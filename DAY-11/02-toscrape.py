import bs4
import requests

# URL de la página de libros
BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"

# Lista para almacenar los títulos de los libros con un rating alto
titulos_alto_rating = []

# Recorremos las páginas de libros
for pagina in range(1, 11):
    # URL de la página actual
    URL_PAGINA = BASE_URL.format(pagina)

    # Crear sopa de la página actual
    resultado = requests.get(URL_PAGINA)
    sopa = bs4.BeautifulSoup(resultado.text, "lxml")
    
    # Obtener todos los libros de la página actual
    libros = sopa.select(".product_pod")

    # Recorremos todos los libros de la página actual
    for libro in libros:
        # Si el libro tiene un rating alto, lo agregamos a la lista
        if len(libro.select(".star-rating.Four")) != 0 or len(libro.select(".star-rating.Five")) != 0:
            # Obtenemos el título del libro
            titulo = libro.select("h3 a")[0].get("title")
            # Agregamos el título a la lista
            titulos_alto_rating.append(titulo)

# Imprimimos la lista de títulos de los libros con un rating alto
for titulo in titulos_alto_rating:
    print(titulo)
