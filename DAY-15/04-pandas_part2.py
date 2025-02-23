import pandas as pd

# Importar "ventas-autos.csv" y convertirlo en un nuevo DATAFRAME
ventas_autos = pd.read_csv("ventas-autos.csv")
print("\n1. DATAFRAME de ventas de autos")
print("-" * 30)
print(ventas_autos)

# Analicemos los tipos de datos disponibles en el dataset de ventas autos
print("\n2. Tipos de datos disponibles en el dataset de ventas autos")
print("-" * 30)
print(ventas_autos.dtypes)

# Apliquemos estadística descriptiva (cantidad de valores, media, desviación estándar, valores mínimos y máximos, cuartiles) al dataset
print("\n3. Apliquemos estadística descriptiva (cantidad de valores, media, desviación estándar, valores mínimos y máximos, cuartiles) al dataset")
print("-" * 30)
print(ventas_autos.describe())

# Obtenemos información del dataset utilizando info()
print("\n4. Obtenemos información del dataset utilizando info()")
print("-" * 30)
print(ventas_autos.info())

# Listamos los nombres de las columnas de nuestro dataset
print("\n5. Listamos los nombres de las columnas de nuestro dataset")
print("-" * 30)
print(ventas_autos.columns)

# Averiguamos el "largo" de nuestro dataset
print("\n6. Averiguamos el \"largo\" de nuestro dataset")
print("-" * 30)
print(len(ventas_autos))

# Mostramos las primeras 5 filas del dataset
print("\n7. Mostramos las primeras 5 filas del dataset")
print("-" * 30)
print(ventas_autos.head())

# Mostramos las primeras 7 filas del dataset
print("\n8. Mostramos las primeras 7 filas del dataset")
print("-" * 30)
print(ventas_autos.head(7))

# Mostramos las últimas 5 filas del dataset
print("\n9. Mostramos las últimas 5 filas del dataset")
print("-" * 30)
print(ventas_autos.tail())

# Utilizamos .loc para seleccionar la fila de índice 3 del DataFrame
print("\n10. Utilizamos .loc para seleccionar la fila de índice 3 del DataFrame")
print("-" * 30)
print(ventas_autos.loc[3])

# Utilizamos .iloc para seleccionar las filas 3, 7 y 9
print("\n11. Utilizamos .iloc para seleccionar las filas 3, 7 y 9")
print("-" * 30)
print(ventas_autos.iloc[[3, 7, 9]])

# Seleccionar la columna "Kilometraje"
print("\n12. Seleccionar la columna \"Kilometraje\"")
print("-" * 30)
print(ventas_autos["Kilometraje"])

# Encontrar el valor medio de la columnas "Kilometraje"
print("\n13. Encontrar el valor medio de la columnas \"Kilometraje\"")
print("-" * 30)
print(ventas_autos["Kilometraje"].mean())

# Seleccionar aquellas columnas que tengan valores superiores a 100,000 kilómetros en la columna Kilometraje
print("\n14. Seleccionar aquellas columnas que tengan valores superiores a 100,000 kilómetros en la columna Kilometraje")
print("-" * 30)
print(ventas_autos[ventas_autos["Kilometraje"] > 100000])

# Creamos una tabla cruzada de doble entrada entre Fabricante y cantidad de puertas
print("\n15. Creamos una tabla cruzada de doble entrada entre Fabricante y cantidad de puertas")
print("-" * 30)
print(pd.crosstab(ventas_autos['Fabricante'], ventas_autos['Puertas']))

# Agrupamos las columnas por fabricante y buscandos el valor medio de las columnas numéricas
print("\n16. Agrupamos las columnas por fabricante y buscandos el valor medio de las columnas numéricas")
print("-" * 30)
columnas_numericas = ventas_autos.select_dtypes(include=['float64', 'int64'])
media_por_fabricante = columnas_numericas.groupby(ventas_autos["Fabricante"]).mean()
print(media_por_fabricante)