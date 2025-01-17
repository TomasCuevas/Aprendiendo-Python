cadena1 = "Hola soy Tomás"
cadena2 = "522258525028"

# Convierte a mayusculas
upper_resultado = cadena1.upper()
print(upper_resultado)

# Convierte a minusculas
lower_resultado = cadena1.lower()
print(lower_resultado)

# Primera letra en mayuscula
capitalize_resultado = cadena1.capitalize()
print(capitalize_resultado)

# Buscamos una cadena en otra cadena, si no hay coincidencia devuelve -1
find_resultado = cadena1.find("Hola")
print(find_resultado)

# Buscamos una cadena en otra cadena, si no hay coincidencia lanza una excepcion
index_resultado = cadena1.index("Hola")
print(index_resultado)

# Si es numerico devuelte True
isnumeric_resultado = cadena2.isnumeric()
print(isnumeric_resultado)

# Si es alfanumerico devuelte True (solo caracteres de la a-z, sin espacios)
isalpha_resultado = cadena1.isalpha()
print(isalpha_resultado)

# Contamos coincidencias de una cadena en otra cadena, devuelve la cantidad de coincidencias
count_resultado = cadena1.count("s")
print(count_resultado)

# Contamos cuantos caracteres tiene una cadena
len_resultado = len(cadena1)
print(len_resultado)

# Verificamos si una cadena empieza con una cadena dada
startswith_resultado = cadena1.startswith("Hola")
print(startswith_resultado)

# Verificamos si una cadena termina con una cadena dada
endswith_resultado = cadena1.endswith("más")
print(endswith_resultado)

# Si el primer argumento se encuentra en la cadena, remplaza el valor de la misma por el segundo argumento dado
replace_resultado = cadena1.replace("Tomás", "Alberto")
print(replace_resultado)

# Separa la cadena en una lista de elementos, por la cadena que le pasemos
split_resultado = cadena1.split(" ")
print(split_resultado)