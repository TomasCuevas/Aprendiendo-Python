# RANDOM: Python nos facilita un módulo (un conjunto de funciones disponibles para su uso) que nos permite generar selecciones pseudo-aleatorias* entre valores o secuencias.

# RANDINT(min, max): devuelve un integer entre dos valores dados (ambos límites incluidos)
# UNIFORM(min, max): devuelve unfloat entre un valor mínimo y uno máximo
# RANDOM(sin parámetros): devuelve un float entre 0 y 1
# CHOICE(secuencia): devuelve une lemento al azar de una secuencia de valores(listas, tuples, rangos, etc.)
# SHUFFLE(secuencia): toma una secuencia de valores mutable (como una lista), y la retorna cambiando el orden de sus elementos aleatoriamente. 

from random import *

aleatorio = randint(1, 50)
print(f"El número aleatorio utilizando RANDINT es: {aleatorio}")

aleatorio = uniform(1, 50)
print(f"El número aleatorio utilizando UNIFORM es: {aleatorio}")

aleatorio = random()
print(f"El número aleatorio utilizando RANDOM es: {aleatorio}")

colores = ["rojo", "verde", "azul", "amarillo", "naranja"]
aleatorio = choice(colores)
print(f"El color aleatorio utilizando CHOICE es: {aleatorio}")

numeros = list(range(5, 51, 5))
shuffle(numeros)
print(f"El orden de los numeros aleatorios utilizando SHUFFLE es: {numeros}")