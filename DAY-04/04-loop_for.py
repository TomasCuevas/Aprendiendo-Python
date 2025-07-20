"""
    # LOOP FOR: 
        Adiferencia de otros lenguajes de programación, los loops for en Python tienen la capacidad de iterar a lo largo 
        de los elementos de cualquier secuencia (listas, strings, entre otros),en el orden en que dichos elementos aparecen.

    # CONCEPTOS
        # LOOPS/BUCLES: son secuencias de instrucciones de código que seejecutan repetidas veces
        # ITERABLES: son objetos en Python que se pueden recorrer (o iterar) a lolargo de sus elementos
"""


lista = ["a", "b", "c"]

for letra in lista:
  print(f"Letra: {letra}")

print("\n")
for letra in lista:
  index = lista.index(letra)
  print(f"Letra: {letra}, Índice: {index}")
  
print("\n")
lista = ["Pablo", "Laura", "Federico", "Luis", "Tomas", "Julia"]
for nombre in lista:
  if nombre.startswith("L"):
    print(f"El nombre comienza con 'L': {nombre}")

print("\n")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mi_valor = 0
for numero in numeros:
  mi_valor += numero
  
print(f"Mi lista de numeros es: {numeros}")
print(f"El valor total de los numeros es: {mi_valor}")
print("\n")

for letra in "Python":
  print(f"Letra: {letra}")

print("\n")
lista = [[1, 2], [3, 4], [5, 6]]
for a, b in lista:
  print(f"a: {a}, b: {b}")

print("\n")
dic = {"clave1": "a", "clave2": "b", "clave3": "c"}
for clave in dic:
  print(clave)

print("\n")
for clave in dic.items():
  print(clave)