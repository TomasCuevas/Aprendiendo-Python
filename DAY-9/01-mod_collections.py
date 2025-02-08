"""
    El módulo Collections amplía los tipos de contenedores
    disponibles en Python. Un contenedor almacena diferentes
    objetos y proporciona una nueva forma de acceder e iterar
    sobre los mismos.

    Counters (Contadores): Es una subclase del diccionario, usado para contar las
    repeticiones de cada elemento en un iterable, en forma de diccionario:

    DefaultDict: Es una subclase del diccionario, usado para proporcionar valores por
    defecto para las claves que no existan, sin generar un mensaje de error. El valor por
    defecto puede ser un tipo de dato (int, list, etc.) o una función lambda que proporcione
    dicho valor directamente (lambda: "mi valor").    

    NamedTuple: devuelve una tupla donde las posiciones de sus elementos tienen un
    nombre, además de un número de índice como las tuplas tradicionales.
"""

from collections import Counter, defaultdict, namedtuple


print("\n" + "=" * 3 + " Utilizando Counter " + "=" * 3)

numeros = [8, 6, 3, 12, 1, 6, 5, 5, 10, 12, 3]
print(f"\nContar repeticiones de cada elemento en un array: {Counter(numeros)}")

frase = "Al pan pan y al vino vino"
print(f"\nContar repeticiones de cada elemento en una frase: {Counter(frase.lower().split())}")

serie = Counter([1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5])
print(f"\nMostrar los elementos más comunes: {serie.most_common()}")
print(f"Mostrar el elemento más común: {serie.most_common(1)}")
print(f"Lista apartir de un diccionario: {list(serie)}")

print("\n" + "=" * 3 + " Utilizando DefaultDict " + "=" * 3)

mi_diccionario = defaultdict(lambda: "valor por defecto")
mi_diccionario["uno"] = "verde"

print(f"\nDiccionario con valor por defecto: {mi_diccionario['dos']}")
print(f"Diccionario: {mi_diccionario}")

print("\n" + "=" * 3 + " Utilizando NamedTuple " + "=" * 3)

Persona = namedtuple("Persona", ["nombre", "edad", "altura"])
ariel = Persona("Ariel", 25, 1.75)

print(f"\nNombre: {ariel.nombre}")
print(f"Edad: {ariel.edad}")
print(f"Altura: {ariel.altura}")










