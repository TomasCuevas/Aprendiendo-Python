"""
    # ENTRADA Y SALIDA DE DATOS:
        La manipulación de archivos desde Python se engloba bajo las funciones de E/S (entrada/salida) o I/O (en inglés:input/output).
        Comenzaremos explorando las funciones utilizadas para abrir, leer y cerrar archivos:

        1. open(archivo, modo): abre un archivo, y devuelve un objeto de tipo archivo sobre el que pueden aplicarse métodos.
        2. read(bytes): devuelve un número especificado de bytes del archivo. De manera predeterminada (sin indicar un valor en el argumento bytes), devolverá el archivo completo (equivalente a escribir -1).
        3. readline(bytes): devuelve una línea del archivo, limitada por el número indicado en el parámetro tamaño (en bytes).
        4. readlines(bytes): devuelve una lista que contiene cada una de las líneas del archivo como item de dicha lista. Si el tamaño excede lo indicado en el parámetro bytes, no se devolverán líneas adicionales.
        5. close(): cierra el archivo abierto, tal que no puede ser leído o escrito luego de cerrado. Es una buena práctica utilizar este método si ya no será necesario realizar acciones sobre un archivo.
"""


mi_archivo = open("prueba.txt")
print("====== read():")
print(mi_archivo.read())
mi_archivo.close()

mi_archivo = open("prueba.txt")
print("\n====== readline():")
print(mi_archivo.readline())
print(mi_archivo.readline())
print(mi_archivo.readline())
mi_archivo.close()

mi_archivo = open("prueba.txt")
print("\n====== readline().rstrip():")
print(mi_archivo.readline().rstrip())
print(mi_archivo.readline().rstrip())
print(mi_archivo.readline().rstrip())
mi_archivo.close()

todas = open("prueba.txt")
print("\n====== readlines():")
print(todas.readlines())
todas.close()

todas = open("prueba.txt")
print("\n====== readlines() con metodo pop():")
print(todas.readlines().pop())
todas.close()
