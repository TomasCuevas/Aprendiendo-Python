# OPERADORES LOGICOS: Estos operadores permiten tomar decisiones basadas enmúltiples condiciones.

# AND devuelve True si todas las condiciones son verdaderas
# OR devuelve True si al menos una condición es verdadera
# NOT devuelve True si el valor del booleano es False, y False si es True

texto = "Esta frase es breve"

mi_booleano = (4 < 5) and (5 > 6)
print(f"4 < 5 and 5 > 6: {mi_booleano}")
print("\n")

mi_booleano = (4 < 5) and (5 == (3 + 2))
print(f"4 < 5 and 5 == (3 + 2): {mi_booleano}")
print("\n")

mi_booleano = (55 == 55) and ("perro" == "perro")
print(f"55 == 55 and 'perro' == 'perro': {mi_booleano}")
print("\n")

mi_booleano = (10 == 10) or (3 == 1)
print(f"10 == 10 or 3 == 1: {mi_booleano}")
print("\n")

mi_booleano = (10 == 5) or ("perro" == "gato")
print(f"10 == 5 or 'perro' == 'gato': {mi_booleano}")
print("\n")

mi_booleano = "frase" in texto
print(f"'frase' in '{texto}': {mi_booleano}")
print("\n")

mi_booleano = ("frase" in texto) and ("breve" in texto)
print(f"'frase' and 'breve' in '{texto}': {mi_booleano}")
print("\n")

mi_booleano = ("frase" in texto) or ("Python" in texto)
print(f"'frase' or 'Python' in '{texto}': {mi_booleano}")
print("\n")

mi_booleano = not ('a' == 'a')
print(f"not 'a' == 'a': {mi_booleano}")
print("\n")

mi_booleano = not ('a' != 'a')
print(f"not 'a' != 'a': {mi_booleano}")
print("\n")
