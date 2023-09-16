# Creando una lista (se pueden modificar)
lista = ["Tomás Cuevas", True, 1.77]

print(lista[1])

lista[2] = 1.80

print (lista)

# Creando una tupla (no se pueden modificar)
tupla = ("Tomás Cuevas", True, 1.77)

print(tupla)

# Creando un conjunto (set) (no se accede a elementos por indice, no almacena datos duplicados)
conjunto = {"Tomás Cuevas", True, 1.77, "Tomás Cuevas"}

print(conjunto)

# Creandun un diccionario (dict)
diccionario = {
  "nombre": "Tomas",
  "apellido": "Cuevas",
  "altura": 1.77
}

print(diccionario["nombre"])
