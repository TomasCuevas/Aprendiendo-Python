"""
    ¡Qué bueno que lograste abrirme!
    Junto a esta nota se ha descomprimido 1 carpeta, y está repletas de subcarpetas y de archivos .txt.
    No te preocupes por revisarlos, solo tienen texto aleatorio... excepto algunos. ¯\\_(ツ)_/¯

    # TAREA:
        Tu trabajo es crear un Buscador de Números de Serie. ¿Qué es eso? Es un programa que se encargue 
        de buscar números de serie que cumplan un determinado formato, dentro de un arbol de carpetas.

        Tu programa va a recorrer todos los archivos y subcarpetas de un directorio raiz (en este caso, 
        la carpeta que acabas de descomprimir), y va a buscar cualquier string que coincida con un patrón 
        de número de serie. Sabemos que no puede haber más de un número de serie por archivo.

        Para lograrlo vas a usar el módulo os para abrir e iterear por el directorio, y las expresiones regulares
        para encontrar el formato de número de serie correcto.

        A los fines de este ejercicio, estas son las condiciones de formato que deben cumplir los hallazgos:
        - [N] + [tres carateres de texto] + [-] + [5 números]

        Por ejemplo: Nryu-12365

        La presentación en pantalla de los hallazgos debe ser un listado en formato de tabla, que respete el siguiente formato de ejemplo:

        ----------------------------------------------------
        Fecha de búsqueda: [fecha de hoy]

        ARCHIVO		NRO. SERIE
        -------		----------
        texto1.txt	Nter-15496
        texto25.txt	Ngba-85235

        Números encontrados: 2
        Duración de la búsqueda: 1 segundos
        ----------------------------------------------------

        IMPORTANTE

        * La 'Duración de búsqueda' debe estar redondeada hacia arriba
        * No olvides que la mejor forma de recorrer un arbol de carpetas, probablemente sea con el método walk() de os.
        * Observa que la fecha de búsqueda debe ser la fecha del día en que ejecutes el código, por lo que necesitas echar mano del módulo datetime.
        * Animate a encontrar una manera de mostrar la fecha de hoy con el formato dd/mm/aa.
        * Para informar la duración de la búsqueda al final de tu presentación, vas a necesitar del módulo time.
        * Recuerda que para poder imprimir todo en formato de tabla puedes usar los caracteres especiales \\t para tabular.
"""


import os
import re
import datetime
import timeit
import math

def obtener_fecha_actual():
    hoy = datetime.datetime.now()
    return f"{hoy.day:02d}/{hoy.month:02d}/{hoy.year}"

def buscar_coincidencias(ruta, patron):
    coincidencias = []
    for carpeta, _subcarpeta, archivos in os.walk(ruta):
        for archivo in archivos:
            ruta_completa = os.path.join(carpeta, archivo)
            with open(ruta_completa, "r", encoding="utf-8") as file:
                contenido = file.read()
                serie = re.search(patron, contenido)
                if serie:
                    coincidencias.append((archivo, serie.group()))

    return coincidencias

def imprimir_resultados(fecha, coincidencias, duracion):
    print("----------------------------------------------------")
    print(f"Fecha de búsqueda: {fecha}\n")
    print("ARCHIVO\t\t\tNRO. SERIE")
    print("-------\t\t\t----------")
    
    for archivo, serie in coincidencias:
        print(f"{archivo}\t\t{serie}")
    
    print(f"\nNúmeros encontrados: {len(coincidencias)}")
    print(f"Duración de la búsqueda: {duracion} segundos")
    print("----------------------------------------------------")

def main():
    inicio = timeit.default_timer()
    
    ruta_raiz = os.path.join(os.getcwd(), "08-task", "mi_gran_directorio")
    patron = r"N[a-zA-Z]{3}-\d{5}"
    fecha_actual = obtener_fecha_actual()
    coincidencias = buscar_coincidencias(ruta_raiz, patron)
    
    duracion = math.ceil(timeit.default_timer() - inicio)
    
    imprimir_resultados(fecha_actual, coincidencias, duracion)

if __name__ == "__main__":
    main()