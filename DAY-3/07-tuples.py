# Los tuples o tuplas, son estructuras de datos que almacenan múltiples elementos en una única variable. Se caracterizan por ser ordenadas e inmutables.  
# Esta característica las hace máseficientes en memoria y a prueba de daños

mi_tupla = (1,2,(10, 20),4)

print(f"Mi tupla es: '{mi_tupla}'")
print("\n")

print(f"El tipo de mi_tuple es '{type(mi_tupla)}'")
print("\n")

print(f"Mi tupla en la posición [2] es {mi_tupla[2]}")
print(f"Mi tupla en la posición [2][0] es {mi_tupla[2][0]}")
print("\n")

mi_tupla = list(mi_tupla)
print(f"Mi tupla convertida a lista es '{mi_tupla}'")
print(f"El tipo de mi_tupla es '{type(mi_tupla)}'")
print("\n")

another_tupla = (5, 6, 7)
print(f"Mi nueva tupla es '{another_tupla}'")
print("\n")

x, y, z = another_tupla
print(f"Desestructurado de tupla en x, y, z = {x}, {y}, {z}")
print("\n")

print(f"Metodo count() de tupla: {another_tupla.count(5)}")
print("\n")

print(f"Metodo index() de tupla: {another_tupla.index(5)}")
print("\n")