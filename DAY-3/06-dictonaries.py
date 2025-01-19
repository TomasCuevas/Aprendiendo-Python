# DICCIONARIOS: Los diccionarios son estructuras de datos que almacenaninformación en pares clave:valor. 
# Son especialmente útiles para guardar y recuperar información a partir de los nombresde sus claves (no utilizan índices).

diccionario = {"c1": "valor 1", "c2": "valor 2"}

print(f"El tipo de diccionario es '{type(diccionario)}'")
print("\n")

print(f"El diccionario es {diccionario}")
print("\n")

resultado = diccionario["c1"]
print(f"El valor de la clave 'c1' es '{resultado}'")
print("\n")

client = {"nombre": "Juan", "apellido": "Perez", "edad": 30, "altura": 1.76, "sexo": "M"}
consulta = client["nombre"]
print(f"El client es {client}")
print(f"El nombre del cliente es '{consulta}")
print("\n")

dic = {"c1": 55, "c2": [10, 20, 30], "c3": {"s1": 100, "s2": 200}}
print(f"El diccionario es {dic}")
print(f"dic['c2'][0] = {dic['c2'][1]}" )
print(f"dic['c3']['s1'] = {dic['c3']['s1']}" )
print("\n")

dic = {"c1": ["a", "b", "c"], "c2": ["d", "e", "f"]}
consulta = dic["c2"][1].upper()
print(f"El diccionario es {dic}")
print(f"El valor de dic['c2'][1] en mayusculas es '{consulta}'")
print("\n")

dic = {1: "a", 2: "b"}
print(f"El diccionario es {dic}")
dic[3] = "c"
print(f"El diccionario con el elemento '3' a 'c' es {dic}")
dic[2] = "B"
print(f"El diccionario con el elemento '2' a 'B' es {dic}")
print("\n")

print(f"Las claves del diccionario son {dic.keys()}")
print(f"Los valores del diccionario son {dic.values()}")
print(f"Los items del diccionario son {dic.items()}")