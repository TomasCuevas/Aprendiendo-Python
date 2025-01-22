# INTERACCION ENTRE FUNCIONES: Las salidas de una determinada función pueden convertirse en entradas de otras funciones. De esa manera, 
# cada función realiza una tarea definida, y el programa se construye a partir de la interacción entre funciones.

from random import shuffle

# Lista inicial
palitos = ['-', '--', '---', '----']

# Mezclar la lista
def mezclar(palitos):
	shuffle(palitos)
	return palitos

# Pedir intento
def probar_suerte():
	intento = ''

	while intento not in ["1", "2", "3", "4"]:
		intento = input("Elige un numero entre 1 y 4: ")
 
	return int(intento)

# Comprobar intento
def chequear_intento(lista, intento):
	if lista[intento - 1] == '-':
		print("\nA lavar los platos.")
	else:
		print("\nEsta vez te has salvado.")

	print(f"Te ha tocado {lista[intento - 1]}.")
 
palitos_mezclados = mezclar(palitos)
intento = probar_suerte()
chequear_intento(palitos_mezclados, intento)