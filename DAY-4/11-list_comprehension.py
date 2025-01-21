# COMPRENSION DE LISTAS: La comprensión de listas ofrece una sintaxis más breve en la creación de una nueva lista basada en valores disponibles en otra secuencia. 
# Vale la pena mencionar que la brevedad se logra a costo de una menor interpretabilidad.

palabra = "Python"
lista = [letra for letra in palabra]
print(lista)

print("\n")
lista = [n for n in range(1, 51, 2)]
print(lista)

print("\n")
lista = [n / 1.25 for n in range(1, 51, 2)] 
print(lista)

print("\n")
lista = [n for n in range(1, 51, 2) if n * 10 > 200]
print(lista)

pies = [10, 20, 30, 40, 50]
metros = [pie / 3.281 for pie in pies]
print(metros)