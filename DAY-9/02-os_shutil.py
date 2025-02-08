"""
    El módulo Shutil ofrece funcionalidades de alto nivel sobre
    archivos, tales como copiar, crear, eliminar y mover entre
    directorios. También mencionaremos métodos del módulo os
    que cumplen objetivos similares.

    # shutil.move(archivo, directorio) : mueve un archivo desde el directorio actual
    hacia aquel que se especifica en el segundo parámetro.
    
    # os.unlink(directorio) : elimina un archivo del directorio indicado

    # os.rmdir(directorio) : elimina una carpeta vacía
    
    # shutil.rmtree(directorio) : elimina una carpeta indicada en el directorio,
    incluyendo todas sus ramificaciones (subcarpetas y archivos), de manera
    definitiva y sin pasar por la papelera de reciclaje.

    # send2trash.send2trash(archivo) : envía un archivo a la papelera de reciclaje (es
    necesario instalar el módulo desde pip install Send2Trash y luego importarlo)

    # os.walk(directorio) : recorre el directorio indicado, y devuelve los nombres de
    carpetas, subcarpetas y archivos dentro de ellas en forma de tupla, a través de un
    generador.
"""

import os
import shutil
import send2trash

print("\nLimpiando archivos...")
send2trash.send2trash("/home/tomascuevas/Desktop/archivo.txt")

print("\nCreando archivo...")
archivo = open("archivo.txt", "w")
archivo.write("Hola, mundo!")
archivo.close()

print("\nMoviendo archivo...")
shutil.move("archivo.txt", "/home/tomascuevas/Desktop/")

print("\nRecorriendo directorio...")
ruta = "/home/tomascuevas/Desktop/carpeta_superior"

for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f"\nEn la carpeta {carpeta} hay:")
    
    print(f"\tSubcarpetas:")
    for sub in subcarpeta:
        print(f"\t\t{sub}")

    print(f"\tArchivos:")
    for arch in archivo:
        print(f"\t\t{arch}")

