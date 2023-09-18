# Creando una lista con (list)
lista = list(["hola", "Tomás", 23])

print(lista)

# Devuelve la cantidad de elementos de la lista
resultado = len(lista)

print(resultado)

# Agregar nuevo elemento a la lista (append)
lista.append("Cuevas")

print(lista)

# Agregar nuevo elemento a la lista en un indice especifico (insert)
lista.insert(2, "Vera")

print(lista)

# Agregar varias elementos a la lista (extend)
lista.extend([False, 2023])

print(lista)

# Eliminar un elemento de la lista por su indice (pop) 
lista.pop(2)

print(lista)

# Remover un elemento de la lista por su valor (remove)
lista.remove(False)

print(lista)

# Eliminar todos los elementos de la lista (clear)
lista.clear()

print(lista)

lista2 = [2023, 23, 52, False, True, 15]

# Ordenar una lista de forma ascendente (sort)
lista2.sort()

print(lista2)

# Ordenas una lista de forma descendente (sort reverse=True)
lista2.sort(reverse=True)

print(lista2)

lista3 = ["Hola", "Tomás", 23, "Vera", "Argentina", 2023]

# Invertir una lista (reverse)
lista3.reverse()

print(lista3)

# Verificar si un elemento existe en la lista (index)
elemento_encontrado = lista3.index("Vera")

print(elemento_encontrado)