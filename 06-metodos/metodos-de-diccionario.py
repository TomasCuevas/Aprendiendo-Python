diccionario = {
  "nombre": "Tomás",
  "apellido": "Dalto",
  "edad": 23
}

print(diccionario)

# Nos devuelve un objeto dic_item
claves = diccionario.keys()
print(claves)

## Obtener un valor (get)
valor_nombre = diccionario.get("nombre")
print(valor_nombre)

# Eliminar un elemento del diccionario (pop)
diccionario.pop("nombre")
print(diccionario)

# Obtener un elemento dict_items iterable
diccionario_iterable = diccionario.items()
print(diccionario_iterable)

# Eliminar todo del diccionario (clear)
diccionario.clear()
print(diccionario)

