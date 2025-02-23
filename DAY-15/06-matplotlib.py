import matplotlib.pyplot as plt
import numpy as np

# Creamos un gráfico utilizando plt.plot()
print("\n1. Creamos un gráfico utilizando plt.plot()")
print("-" * 30)
plt.plot()
plt.show()

# Graficomos una lista de números
print("\n2. Graficomos una lista de números")
print("-" * 30)
a = [1,5,3,8,7,15]
plt.plot(a)
plt.show()

# Creamos dos listas, x e y. Llenamos a la lista x de valores del 1 al 100.
print("\n3. Creamos dos listas, x e y. Llenamos a la lista x de valores del 1 al 100.")
print("-" * 30)
x = list(range(101))

# Los valores de y van a equivaler al cuadrado del respectivo valor en x con el mísmo índice
y = [i**2 for i in x]

# Graficamos ambas listas creadas
plt.plot(x, y)
plt.show()

# Creamos el gráfico utilizando plt.subplots()
print("\n4. Creamos el gráfico utilizando plt.subplots()")
print("-" * 30)
fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()

# Preparar los datos
print("\n5. Flujo de trabajo en Matplotlib")
print("-" * 30)
x = list(range(101))
y = [i**2 for i in x]

# Preparamos el área del gráfico (fig) y el gráfico en sí (ax) utilizando plt.subplots()
fig, ax = plt.subplots()

# Añadimos los datos al gráfico
ax.plot(x, y)

# Personalizamos el gráfico añadiendo título al gráfico y a los ejes x e y
ax.set(title= 'Grafico de casos de COVID 19 en Latam', xlabel= 'dias', ylabel= 'casos confirmados')
plt.show()

#creamos un nuveo set de datos utilizando la librería Numpy
print("\n6. Creamos un nuveo set de datos utilizando la librería Numpy")
print("-" * 30)
x1 = np.linspace(0, 100, 20)
y1 = x1**2

# Creamos el gráfico de dispersión de x vs y
fig, ax = plt.subplots()
ax.scatter(x1, y1)
plt.show()

# Visualizamos ahora la función seno, utilizando np.sin(X)
print("\n7. Visualizamos ahora la función seno, utilizando np.sin(X)")
print("-" * 30)
fix, ax = plt.subplots()
x2 = np.linspace(-10, 10, 100)
y2 = np.sin(x2)

ax.scatter(x2, y2)
plt.show()