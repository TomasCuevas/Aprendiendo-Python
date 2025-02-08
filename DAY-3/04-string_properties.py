"""
    # PROPIEDADES DE LOS STRINGS: 
        son inmutables: una vez creados, no pueden modificarse sus partes,pero sí pueden reasignarse los valores de las variables a través demétodos de strings
        concatenable: es posible unir strings con el símbolo +
        multiplicable: es posible concatenar repeticiones de un string con elsímbolo *
        multilineales: pueden escribirse en varias líneas al encerrarse entretriples comillas simples (''' ''') o dobles (""" """)
"""


# son inmutables: una vez creados, no pueden modificarse sus partes,pero sí pueden reasignarse los valores de las variables a través demétodos de strings
nombre = "Carina"
# nombre[0] = "K" -> ERROR
nombre = f"K{nombre[1:]}"
print(nombre)
print("\n")

# concatenable: es posible unir strings con el símbolo +
n1 = "Kari"
n2 = "na"
print(n1 + n2)
print("\n")

# multiplicable: es posible concatenar repeticiones de un string con elsímbolo *
print(n1 * 5)
print("\n")

# multilineales: pueden escribirse en varias líneas al encerrarse entretriples comillas simples (''' ''') o dobles (""" """)
poema = """Mil pequeños peces blancos
como si hirviera
en el color del agua
"""""

print(poema)
print("\n")

# verificar su contenido: a través de las palabras clave in y not in. El resultado de esta verificación es un booleano (True/False).
print(f"'agua' in poema: {'agua' in poema}")
print(f"fuego not in poema: {'fuego' not in poema}")
print("\n")

# determinar su longitud: a través de la función len (mi_string)
print(f"La longitud del poema es {len(poema)}")