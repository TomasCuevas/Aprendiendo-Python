import numpy as np

# Podemos crear arrays de una dimensión con la función np.array()
array_unidim = np.array([1, 2, 3, 4, 5])

# O un array de dos dimensiones (bidimensional)
array_bidim = np.array([[1, 2], [3, 4]])

# O un array de tres dimensiones (tridimensional)
array_tridim = np.array([[[1, 2], [2, 3]], [[4, 5], [6, 7]]])

# Para cada uno de estos arrays, podemos obtener sus propiedades, tales como su "forma", número de dimensiones, tipos de datos y tamaño.

# Atributos del array unidimensional (forma, número de dimensiones, tipos de datos, tamaño, y tipo)
print("\n1. Atributos del array unidimensional")
print(array_unidim.shape, array_unidim.ndim, array_unidim.dtype, array_unidim.size, type(array_unidim))

# Atributos del array bidimensional
print("\n2. Atributos del array bidimensional")
print(array_bidim.shape, array_bidim.ndim, array_bidim.dtype, array_bidim.size, type(array_unidim))

# Atributos del array tridimensional
print("\n3. Atributos del array tridimensional")
print(array_tridim.shape, array_tridim.ndim, array_tridim.dtype, array_tridim.size, type(array_unidim))

# Creamos un array de tamaño 4x3, formado únicamente por unos (1)
unos = np.ones((4, 3))
print("\n4. Array de unos de tamaño (2, 5)")
print(unos)

# Creamos un array de tamaño 2x4x3, formado únicamente por ceros (0)
cero = np.zeros((2, 4, 3))
print("\n5. Array de ceros de tamaño (2, 4, 3)")
print(cero)

# Creamos un array de números en el rango de 0 a 100, con un paso de 5
array_1 = np.arange(0, 100, 5)
print("\n6. Array de números en el rango de 0 a 100, con un paso de 5")
print(array_1)

# Creamos un array de números aleatorios enteros comprendidos en entre 0 y 10, de tamaño (2, 5)
array_2 = np.random.randint(0, 10, (2, 5))
print("\n7. Array de números aleatorios enteros comprendidos en entre 0 y 10, de tamaño (2, 5)")
print(array_2)

# Creamos un array de números aleatorios decimales comprendidos en entre 0 y 1, de tamaño (3, 5)
array_3 = np.random.random((3, 5))
print("\n8. Array de números aleatorios decimales comprendidos en entre 0 y 1, de tamaño (3, 5)")
print(array_3)