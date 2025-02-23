import numpy as np

# Establecemos la "semilla" de números aleatorios en 27
np.random.seed(27)

# Creamos un array de números aleatorios enteros comprendidos en entre 0 y 10, de tamaño (3, 5)
array_1 = np.random.randint(0, 10, (3,5))
print("\n1. Array de números aleatorios enteros comprendidos en entre 0 y 10, de tamaño (3, 5)")
print("-" * 30)
print(array_1)

# Encontramos los valores únicos del array_1
print("\n2. Encontramos los valores únicos del array anterior")
print("-" * 30)
print(np.unique(array_1))

# Extraemos el elemento de índice 1 del array_1
print("\n3. Extraemos el elemento de índice 1 del array anterior")
print("-" * 30)
print(array_1[1])

# Extraemos las primeras dos filas del array_1
print("\n4. Extraemos las primeras dos filas del array anterior")
print("-" * 30)
print(array_1[:2])

# Extraemos los dos primeros datos de las primeras dos filas del array_4
print("\n5. Extraemos los dos primeros datos de las primeras dos filas del array anterior")
print("-" * 30)
print(array_1[:2, :2])

# Creamos dos arrays de tamaño 3x4: uno relleno de números aleatorios entre 0 y 10, y otro relleno de unos
print("\n6. Creamos dos arrays de tamaño (3x4) uno relleno de números aleatorios entre 0 y 10, y otro relleno de unos")
print("-" * 30)
array_2 = np.random.randint(0, 10, (3, 4))
array_3 = np.ones((3, 4))

print(array_2)
print("\n")
print(array_3)

# Sumamos los dos arrays
print("\n7. Sumamos los dos arrays")
print("-" * 30)
print(array_2 + array_3)

# Creamos otros dos arrays de tamaño 3x3 con números aleatorios del 1 al 5
print("\n8. Creamos otros dos arrays de tamaño (3x3) con números aleatorios del 1 al 5")
print("-" * 30)
array_4 = np.random.randint(1, 5, (3, 3))
array_5 = np.random.randint(1, 5, (3, 3))

print(array_4)
print("\n")
print(array_5)

# Multiplicamos los últimos dos arrays entre sí
print("\n9. Multiplicamos los dos arrays anteriores entre sí")
print("-" * 30)
print(array_4 * array_5)

# Elevamos el array_4 al cuadrado
print("\n10. Elevamos el array anterior al cuadrado")
print("-" * 30)
print(array_4 ** 2)

# Buscamos la raíz cuadrada del array_5
print("\n11. Buscamos la raíz cuadrada del array anterior")
print("-" * 30)
print(np.sqrt(array_5))

# Hallamos el promedio de los valores del array_5
print("\n12. Hallamos el promedio de los valores del array anterior")
print("-" * 30)
print(np.mean(array_5))

# Hallamos el valor máximo y mínimo de los valores del array_5
print("\n13. Hallamos el valor máximo y mínimo de los valores del array anterior")
print("-" * 30)
print(f"Máximo: {np.max(array_5)}, Mínimo: {np.min(array_5)}")

# Ordenamos de menor a mayor los elementos dentro del array_4
print("\n14. Ordenamos de menor a mayor los elementos dentro del array anterior")
print("-" * 30)
print(np.sort(array_4))