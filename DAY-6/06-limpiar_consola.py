"""
    # LIMPIAR LA CONSOLA:
        Para controlar la información mostrada al usuario en consola podemos limpiarla, eliminando los diferentes 
        mensajes que han aparecido conforme se va ejecutando el programa.
"""


from os import system

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

system("cls")

print(f"Hola {nombre}, tu edad es {edad}")
