# INTEGERS & FLOATS: Existen dos tipos de datos numéricos básicos en Python: int y float. Como toda variable en Python, 
# su tipo queda definido al asignarle un valor a una variable. La función type() nos permite obtener el tipo de valor almacenado en una variable. 

# INT: o integer, es un número entero, positivo o negativo, sin decimales, de un largo indeterminado.

# FLOAT: o "número de punto flotante" es un número que puede ser positivo o negativo, que a su vez contiene una o más posiciones decimales. 

mi_numero = 1 + 3
print(mi_numero + mi_numero)
print(type(mi_numero))
print("\n")

mi_numero_float = 5.8
print(mi_numero_float)
print(type(mi_numero_float))
print("\n")

mi_numero_float = 1 + 5.8
print(mi_numero_float)
print(type(mi_numero_float))
print("\n")

edad = input('Escribe tu edad: ')
print("Tu edad es " + edad)
print(type(edad))