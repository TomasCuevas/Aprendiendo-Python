"""
    # MIN(): 
        La función min() retorna el item con el valor más bajo dentro de un iterable. 
    # MAX(): 
        La función max() funciona del mismo modo, devolviendo el valor más alto del iterable. 
        Si el iterable contiene strings, la comparación se realiza alfabéticamente.
"""

lista = [59, 45, 78, 12, 34]
menor = min(lista)
mayor = max(lista)

print(f"La lista es: {lista} \n")

print(f"El menor valor es {menor}")
print(f"El mayor valor es {mayor}")

nombres = ["Juan", "Tomas", "Maria", "Pedro", "Luis"]
menor_nombre = min(nombres)
mayor_nombre = max(nombres)

print(f"\nLos nombres son: {nombres} \n")

print(f"El menor nombre ordenado de forma alfabética es '{menor_nombre}'")
print(f"El mayor nombre ordenado de forma alfabética es '{mayor_nombre}'")

nombre = "Tomas"
menor_letra = min(nombre.lower())
mayor_letra = max(nombre.lower())

print(f"\nEl nombre es: {nombre} \n")

print(f"La letra menor ordena de forma alfabética es '{menor_letra}'")
print(f"La letra mayor ordena de forma alfabética es '{mayor_letra}'")

dic = {"C1": 45, "C2": 78}
minimo_del_diccionario = min(dic.values())
maximo_del_diccionario = max(dic.values())

print(f"\nEl diccionario es: {dic} \n")

print(f"El mínimo de los valores del diccionario es {minimo_del_diccionario}")
print(f"El máximo de los valores del diccionario es {maximo_del_diccionario}")