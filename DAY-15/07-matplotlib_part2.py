import matplotlib.pyplot as plt
import numpy as np

# Creemos un diccionario con tres platos y su respectivo precio
# Las claves del diccionario serán los nombres de las comidas, y los valores asociados, su precio
comidas = {'lasagna': 350, 'sopa': 150, 'roast beef': 650}

# Crearemos un gráfico de barras donde el eje x está formado por las claves del diccionario,
# y el eje y contiene los valores.
print("\n1. Crearemos un gráfico de barras donde el eje x está formado por las claves del diccionario, y el eje y contiene los valores.")
print("-" * 30)
fig, ax = plt.subplots()
ax.bar(comidas.keys(), comidas.values())

# Añadimos los títulos correspondientes
ax.set(title= 'Precios de comidas', xlabel= 'Comidas', ylabel= 'Precios')
plt.show()

# Probemos a continuación con un gráfico de barras horizontales
print("\n2. Probemos a continuación con un gráfico de barras horizontales")
print("-" * 30)
fig, ax = plt.subplots()
ax.barh(comidas.keys(), comidas.values())
ax.set(title= 'Precios de comidas', ylabel= 'Comidas', xlabel= 'Precios')
plt.show()

# Creamos una distribución de 1000 valores aleatorios distribuidos normalmente
print("\n3. Creamos una distribución de 1000 valores aleatorios distribuidos normalmente")
print("-" * 30)
x = np.random.randn(1000)

# Creamos el histograma
fig, ax = plt.subplots()
ax.hist(x)
plt.show()

# Creamos la misma disposición de gráficos, con un tamaño de figura de 10x5
print("\n4. Creamos la misma disposición de gráficos, con un tamaño de figura de 10x5")
print("-" * 30)
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(10,5))

# Para nuestro primer gráfico, tomamos el conjunto x_1, y_1, y generamos un gráfico de líneas
x1 = np.linspace(0, 100, 20)
y1 = x1**2
ax1.plot(x1, y1)

# Para nuestro segundo gráfico, tomamos el conjunto x_2, y_2, y generamos un gráfico de dispersión
x2 = np.linspace(-10, 10, 100)
y2 = np.sin(x2)
ax2.scatter(x2, y2)

# Creamos un gráfico con los precios de tres comidas en la esquina inferior izquierda
ax3.bar(comidas.keys(), comidas.values())

# El gráfico de la esquina inferior derecha será un histograma de valores aleatorios con distribución normal
ax4.hist(np.random.randn(1000))
plt.show()

# Cambiamos el estilo predeterminado por "seaborn-v0_8-whitegrids"
print("\n5. Cambiamos el estilo predeterminado por \"seaborn-v0_8-whitegrid\"")
print("-" * 30)
plt.style.use('seaborn-v0_8-whitegrid')

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(10,5))

# Para nuestro primer gráfico, tomamos el conjunto x_1, y_1, y generamos un gráfico de líneas
x1 = np.linspace(0, 100, 20)
y1 = x1**2
ax1.plot(x1, y1)

# Para nuestro segundo gráfico, tomamos el conjunto x_2, y_2, y generamos un gráfico de dispersión
x2 = np.linspace(-10, 10, 100)
y2 = np.sin(x2)
ax2.scatter(x2, y2)

# Creamos un gráfico con los precios de tres comidas en la esquina inferior izquierda
ax3.bar(comidas.keys(), comidas.values())

# El gráfico de la esquina inferior derecha será un histograma de valores aleatorios con distribución normal
ax4.hist(np.random.randn(1000))
plt.show()