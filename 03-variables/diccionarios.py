# Crear diccionario con dic()
diccionario = dict(nombre="Tomás", apellido="Cuevas")
print(diccionario)

# Listas no pueden ser claves y usamos frontset para meter conjuntos
diccionario2 = {frozenset(["Tomás", "Cuevas"]): "Jajja"}
print(diccionario2)

# Crear diccionario con fromkeys() valor por defecto: none
diccionario3 = dict.fromkeys(["nombre", "apellido"])
print(diccionario3)

# Crear diccionario con fromkeys() cambiando el valor por defecto a: No se
diccionario4 = dict.fromkeys(["nombre", "apellido"], "No se")
print(diccionario4)