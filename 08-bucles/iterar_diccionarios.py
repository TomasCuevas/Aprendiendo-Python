diccionario = {"nombre": "Tomás", "apellido": "Cuevas", "edad": 23}

# Recorriendo diccionario para obtener las claves
for key in diccionario:
  print(key)

# Recorriendo diccionario con .items() para obtener la clave y el valor
for [key, value] in diccionario.items():
  print(f"La clave es: {key} el valor es: {value}")