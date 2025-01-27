# Trabajar sobre archivos que se encuentran en directorios diferentes al de nuestro código requiere del soporte del módulo OS,
# que contiene una serie de funciones para interactuar con el sistema operativo.

# os.getcwd(): obtiene y devuelve el directorio de trabajo actual. Será el mismo en el que corre el programa si no se ha modificado.
# os.chdir(ruta): cambia el directorio de trabajo a la ruta especificada.
# os.makedirs(ruta): crea una carpeta, así como todas las carpetas intermedias necesarias de acuerdo a la ruta especificada.
# os.path.basename(ruta): dada una ruta, obtiene el nombre del archivo (nombre de base)
# os.path.dirname(ruta): dada una ruta, obtiene el directorio (carpeta) que almacena el archivo
# os.path.split(ruta): devuelve una tupla que contiene dos  elementos: el directorio, y el nombre de base del archivo.
# rmdir(ruta): elimina el directorio indicado en la ruta.

# En Windows, es necesario indicar las rutas con dobles barras invertidas (\\) para que sean correctamente interpretadas por Python.

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
