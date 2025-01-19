# INDEX(): Utilizamos el método index() para explorar strings, ya quepermite hallar el índice
# de aparición de un caracter o cadena decaracteres dentro de un texto dado.

mi_texto = "Esta es una prueba"

resultado = mi_texto[3]
print(f"El caracter del texto en la posición 3 es '{resultado}'")
print("\n")

resultado = mi_texto[-4]
print(f"El caracter del texto en la posición -4 es '{resultado}'")
print("\n")

resultado = mi_texto.index("n")
print(f"El caracter del texto en la posición {resultado} es 'n'")
print("\n")

resultado = mi_texto.index("prueba")
print(f"La palabra 'prueba' comienza en la posición {resultado}")
print("\n")

resultado = mi_texto.index("a", 5, 12)
print(f"La primera letra 'a' comenzando desde la posición 5 se encuentra en la posición {resultado}")
print("\n")

resultado = mi_texto.rindex("a")
print(f"La última letra 'a' se encuentra en la posición {resultado}")
print("\n")