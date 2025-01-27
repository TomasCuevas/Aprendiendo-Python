# Para escribir en un archivo desde Python, deberemos elegir con cuidado el parámetro "modo de apertura".

# Parámetros de modo de apertura:

# "r" - Read (Lectura) - Predeterminado. Permite leer pero no escribir, y arroja un error si el archivo no existe.
# "a" - Append (Añadir) - Abre el archivo para añadir líneas acontinuación de la última que ya exista en el mismo. Crea un archivo en caso de que el mismo no exista.
# "w" - Write (Escritura) - Abre o crea un archivo (si no existe previamente) en modo de escritura, lo que significa que cualquier contenido previo se sobreescribirá.
# "x" - Create (Creación) - Crea un archivo, y arroja un error si el mismo ya existe en el directorio.

# El método write() escribe un texto especificado en el argumento sobre el archivo.
# writelines(lista) recibe el texto a ser escrito en forma de lista.

mi_archivo = open("prueba.txt", "w")
print("====== open(file, 'w') con metodo write():")
mi_archivo.write("Hola\n")
mi_archivo.write("Este es el nuevo texto para el archivo 'prueba.txt'")
mi_archivo.close()

mi_archivo = open("prueba2.txt", "a")
print("\n====== open(file, 'a') con metodo write():")
mi_archivo.write("Creo un archivo nuevo llamado 'prueba2.txt'\n")
mi_archivo.close()

mi_archivo = open("prueba3.txt", "w")
print("\n====== open(file, 'w') con metodo writelines():")
mi_archivo.writelines(["Hola", "Mundo", "Aqui", "Estoy"])
mi_archivo.close()

mi_archivo = open("prueba2.txt", "a")
print("\n====== open(file, 'a') con metodo write():")
mi_archivo.write("Este texto se añadirá al final del archivo")
mi_archivo.close()
