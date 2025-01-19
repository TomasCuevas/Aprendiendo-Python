mi_lista = ["a", "b", "c", "d"]
mi_lista_2 = ["e", "f", "g", "h"]
print(f"La lista mi_lista es '{mi_lista}'")
print(f"La lista mi_lista_2 es '{mi_lista_2}'")
print("\n")

print(f"Tipo de la lista: {type(mi_lista)}")
print("\n")

resultado = len(mi_lista)
print(f"La longitud de la lista es {resultado}")
print("\n")

resultado = mi_lista[1]
print(f"El elemento en el indice 1 es '{resultado}'")
print("\n")

resultado = mi_lista[1:3]
print(f"La lista desde el indice 1 hasta el 3 es '{resultado}'")
print("\n")

mi_lista_3 = mi_lista + mi_lista_2
print(f"La lista 'mi_lista' + 'mi_lista_2' es '{mi_lista_3}'")
print("\n")

mi_lista[3] = "z"
print(f"Se ha cambiado el elemento en el indice 3 a 'z' {mi_lista}")
print("\n")

mi_lista_3.append("y")
print(f"Se ha añadido el elemento 'y' al final de la lista {mi_lista_3}")
print("\n")

mi_lista_3.pop()
print(f"Se ha eliminado el último elemento de la lista {mi_lista_3}")
print("\n")

eliminado = mi_lista_3.pop(0)
print(f"Se ha eliminado el primer elemento de la lista {mi_lista_3}")
print(f"El elemento eliminado es '{eliminado}'")
print("\n")

unorder_list = ["h", "t", "a", "i", "x", "m"]
unorder_list.sort()
print(f"La lista 'unorder_list' ordenada es '{unorder_list}'")
print("\n")

unorder_list.reverse()
print(f"La lista 'unorder_list' invertida es '{unorder_list}'")
print("\n")