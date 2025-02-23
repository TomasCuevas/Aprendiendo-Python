import pandas as pd

# Creamos una serie de números
numeros = pd.Series([1,2,3,4,5,67,35,235,62])
print("\n1. Serie de números")
print("-" * 30)
print(numeros)

# Obtenemos la media de los números
print("\n2. Media de los números")
print("-" * 30)
print(numeros.mean())

# Obtenemos la suma de los números
print("\n3. Suma de los números")
print("-" * 30)
print(numeros.sum())

# Creamos una SERIE de tres colores diferentes
colores = pd.Series(['rojo', 'amarillo', 'verde'])
print("\n4. Serie de tres colores")
print("-" * 30)
print(colores)

# Creamos una serie con tipos de autos, y la visualizamos
tipos_autos = pd.Series(['sedan', 'SUV', 'Pick Up'])
print("\n5. Serie de tipos de autos")
print("-" * 30)
print(tipos_autos)

# Combinamos las series de tipos de autos y colores en un DATAFRAME
tabla_autos = pd.DataFrame({ 'Tipo de Auto': tipos_autos, 'Color': colores })
print("\n6. Dataframe con tipos de autos y colores")
print("-" * 30)
print(tabla_autos)