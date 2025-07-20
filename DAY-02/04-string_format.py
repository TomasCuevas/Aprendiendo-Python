"""
    # FORMATEO DE STRINGS: 
        Para facilitar la concatenación de variables y texto en Python, contamos con dos herramientas 
        que nos evitan manipular las variables, para incorporarlas directamente al texto:

    # FORMAT: 
        se encierra las posiciones de las variables entre corchetes { }, y a continuación del string llamamos a las variables con la función format

    # F-STRINGS: 
        A partir de Python 3.8, podemos anticipar la concatenación de variables anteponiendo 'f' al string
"""


x = 10
y = 5

print("Mis numeros son " + str(x) + " y " + str(y) + " (con STR)")
print("Mis numeros son {} y {} (con FORMAT)".format(x, y))
print(f"Mis numeros son {x} y {y} (con F-STRING)")
print("\n")

print("La suma de " + str(x) + " y " + str(y) + " es " + str(x + y) + " (con STR)")
print("La suma de {} y {} es {} (con FORMAT)".format(x, y, x + y))
print(f"La suma de {x} y {y} es {x + y} (con F-STRING)")
print("\n")

color = 'rojo'
matricula = 543216

print(f"El auto es {color} y su matricula es {matricula}")