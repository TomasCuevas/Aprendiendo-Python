import pandas as pd

ventas_autos = pd.read_csv("ventas-autos.csv")

# Importamos Matplotlib y creamos un gráfico con los valores de la columna Kilometraje
import matplotlib as plt

print("\n1. Importamos Matplotlib y creamos un gráfico con los valores de la columna Kilometraje")
print("-" * 30)
print(ventas_autos["Kilometraje"].plot())

# Puede que un gráfico más apropiado en este caso sea un histograma?
print("\n2. Puede que un gráfico más apropiado en este caso sea un histograma?")
print("-" * 30)
print(ventas_autos['Kilometraje'].hist())

# Elimina la puntuación de la columna de precios
print("\n3. Elimina la puntuación de la columna de precios")
print("-" * 30)
ventas_autos['Precio (USD)'] = ventas_autos['Precio (USD)'].replace('[\,\$\.]','', regex=True).astype(int)/100
print(ventas_autos['Precio (USD)'].plot())