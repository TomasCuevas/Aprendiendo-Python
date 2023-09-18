lista_animales = {"gato", "perro", "loro", "vaca"} 
lista_numeros = {10, 62, 12, 72}

# Recorrer lista_animales
for animal in lista_animales:
  print(animal)

# Recorrer lista_numeros
for numero in lista_numeros:
  resultado = numero * 10
  print(f"{numero}*10 = {resultado}")

# Iterar dos o mas listas del mismo tamaño al mismo tiempo
for numero, animal in zip(lista_numeros, lista_animales):
  print(f"Recorriendo lista_numeros: {numero}")
  print(f"Recorriendo lista_animales: {animal}")

# Forma correcta de recorrer una lista con su indice
for [indice, num] in enumerate(lista_numeros):
  print(num)

# Usar el for/else
for numero in lista_numeros:
  print(f"Ejecutando el codigo: {numero}")
else:
  print("Termino")