"""
    # SETS: 
        Los sets son otro tipo de estructuras de datos. Se diferencian de listas, tuplas y diccionarios 
        porque son una colección mutable de elementos inmutables , no ordenados y sin datos repetidos.
"""


mi_set = set([1, 2, 3, 4, 5])
print(f"Mi set es: {mi_set}")
print(f"El tipo de mi_set es: {type(mi_set)}")
print("\n")

otro_set = {6, 7, 8}
print(f"Otro set es: {otro_set}")
print(f"El tipo de otro_set es: {type(otro_set)}")
print("\n")

print(f"Mi set tiene {len(mi_set)} elementos")
print("\n")

print(f"2 se encuentra en mi_set: {2 in mi_set}")
print("\n")

tercer_set = mi_set.union(otro_set)
print(f"Metodo union() de mi_set con otro_set: {tercer_set}")
print("\n")

mi_set.add(10)
print(f"Agregar 10 a mi_set con el metodo add(): {mi_set}")
print("\n")

mi_set.remove(10)
print(f"Eliminar 10 a mi_set con el metodo remove(): {mi_set}")
print("\n")

mi_set.discard(10)
print(f"Eliminar 10 a mi_set con el metodo discard(): {mi_set}")
print("\n")

mi_set.pop()
print(f"Eliminar el primer elemento de mi_set con el metodo pop(): {mi_set}")
print("\n")

mi_set.clear()
print(f"Eliminar todos los elementos de mi_set con el metodo clear(): {mi_set}")
