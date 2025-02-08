"""
    # TRABAJAR SOBRE ARCHIVOS QUE SE ENCUENTRAN EN DIRECTORIOS DIFERENTES AL DE NUESTRO CÓDIGO REQUIERE DEL SOPORTE DEL MÓDULO OS,
    QUE CONTIENE UNA SERIE DE FUNCIONES PARA INTERACTUAR CON EL SISTEMA OPERATIVO.
    
    # Métodos de OS:
        1. os.getcwd(): obtiene y devuelve el directorio de trabajo actual. Será el mismo en el que corre el programa si no se ha modificado.
        2. os.chdir(ruta): cambia el directorio de trabajo a la ruta especificada.
        3. os.makedirs(ruta): crea una carpeta, así como todas las carpetas intermedias necesarias de acuerdo a la ruta especificada.
        4. os.path.basename(ruta): dada una ruta, obtiene el nombre del archivo (nombre de base)
        5. os.path.dirname(ruta): dada una ruta, obtiene el directorio (carpeta) que almacena el archivo
        6. os.path.split(ruta): devuelve una tupla que contiene dos  elementos: el directorio, y el nombre de base del archivo.
        7. rmdir(ruta): elimina el directorio indicado en la ruta.

    # En Windows, es necesario indicar las rutas con dobles barras invertidas (\\) para que sean correctamente interpretadas por Python.
"""


import os
from pathlib import Path

print("\n===== os.getcwd():")
ruta = os.getcwd()
print(f"Ruta actual: {ruta}")

print("\n===== os.chdir():")
ruta = os.chdir("C:\\Users\\Tomas\\workspace\\guia-cursos\\Aprendiendo-Python\\DAY-5")
archivo = open("02-return.py")
print(f"Archivo seleccionado en la nueva ruta: {archivo}")
archivo.close()

print("\n===== os.makedirs():")
ruta = os.makedirs(
    "C:\\Users\\Tomas\\workspace\\guia-cursos\\Aprendiendo-Python\\DAY-6\\directorio_nuevo"
)
print(f"Directorio creado: {ruta}")

print("\n===== os.rmdir():")
os.rmdir(
    "C:\\Users\\Tomas\\workspace\\guia-cursos\\Aprendiendo-Python\\DAY-6\\directorio_nuevo"
)

print("\n===== os.path.basename():")
ruta = "C:\\Users\\Tomas\\workspace\\guia-cursos\\Aprendiendo-Python\\DAY-6\\prueba.txt"
elemento = os.path.basename(ruta)
print(f"Nombre del archivo: {elemento}")

print("\n===== os.path.dirname():")
elemento = os.path.dirname(ruta)
print(f"Directorio del archivo: {elemento}")

print("\n===== os.path.split():")
elemento = os.path.split(ruta)
print(f"Directorio y archivo: {elemento}")

print("\n===== open('ruta'):")
otro_archivo = open(
    "C:\\Users\\Tomas\\workspace\\guia-cursos\\Aprendiendo-Python\\DAY-6\\prueba3.txt"
)
print(otro_archivo.read())
otro_archivo.close()

print("\n===== Path('ruta'):")
carpeta = Path("C:/Users/Tomas/workspace/guia-cursos/Aprendiendo-Python/DAY-6")
archivo = carpeta / "prueba.txt"
mi_archivo = open(archivo)
print(mi_archivo.read())
