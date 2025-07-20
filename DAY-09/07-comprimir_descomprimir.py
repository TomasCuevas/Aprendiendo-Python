"""
    # COMPRIMIR Y DESCOMPRIMIR ARCHIVOS:
        El formato zip permite comprimir archivos sin pérdida de
        información, ahorrando espacio de almacenamiento y
        manteniendo documentos relacionados en un mismo archivo .zip.

        # Utilizando el módulo zipfile: import zipfile
            # Comprimir archivo:
                mi_zip = zipfile.ZipFile("archivo_comprimido.zip", "w") -> Modo escritura
                mi_zip.write("mi_archivo.txt") -> Comprimir archivo en mi_zip
                mi_zip.close() -> Cerrar archivo zip

            # Descomprimir archivo:
                mi_zip = zipfile.ZipFile("archivo_comprimido.zip", "r") -> Modo lectura
                mi_zip.extractall() -> Extraer todos los archivos de mi_zip
                mi_zip.extract("mi_archivo.txt") -> Extraer un archivo específico de mi_zip
                mi_zip.close() -> Cerrar archivo zip

        #  Utilizando el módulo shutil: import shutil
            # Comprimir archivos:
                shutil.make_archive(archivo_destino, "zip", carpeta_origen)

            # Descomprimir archivos:
                shutil.unpack_archive(archivo_zip, nombre_carpeta_extraccion, "zip)
"""


import zipfile
import send2trash

print("\nLimpiando archivos...")
try:
    send2trash.send2trash("07-archivo_comprimido.zip")
except:
    pass

print("\nCreando archivo...")
mi_zip = zipfile.ZipFile("07-archivo_comprimido.zip", "w")
mi_zip.write("07-mi_texto_a.txt")
mi_zip.write("07-mi_texto_b.txt")
mi_zip.close()

print("\nDescomprimiendo archivo...")
zip_abierto = zipfile.ZipFile("07-archivo_comprimido.zip", "r")
zip_abierto.extractall("07-textos_descomprimidos")
zip_abierto.close()

