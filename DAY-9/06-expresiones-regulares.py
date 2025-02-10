"""
    # EXPRESIONES REGULARES:
        Una expresión regular es una secuencia de caracteres que
        forman un patrón de búsqueda determinado. Pueden ser
        utilizadas para verificar strings en búsqueda de un contenido
        (patrón) específico. Utilizamos el módulo re en Python.

        # Funciones:
            - search( ): devuelve un objeto "match" que contiene información acerca del hallazgo si se encuentra en algún punto del string
            - findall( ): devuelve una lista que contiene todos los hallazgos del patrón

        # Para formar patrones, utilizamos los siguientes cuantificadores y caracteres especiales:
            [] -> Conjunto de caracteres
            [^] -> Conjunto de caracteres negado
            . -> Cualquier caracter
            ^ -> Inicia con
            $ -> Finaliza con
            * -> Cero o más ocurrencias
            + -> Una o más ocurrencias
            {} -> Un número específico de ocurrencias
            ? -> Ocurre una vez o ninguna
            | -> Operador lógico O
            
            \\d -> Dígito numérico
            \\D -> No numérico
            \\w -> Caracter alfanumérico
            \\W -> No alfanumérico
            \\s -> Espacio en blanco
            \\S -> No espacio en blanco
"""

import re

texto = "Si necesitas ayuda llama al (658)-555-0113 las 24 horas al servicio de ayuda online"
print(f"Texto: {texto}\n\n")

palabra = "ayuda" in texto
print(f"Se encuentra la palabra 'ayuda' en el texto: {palabra}")

patron = "nada"

busqueda = re.search(patron, texto)
print(f"Se encuentra la palabra '{patron}' en el texto: {busqueda}")

patron = "necesitas"

busqueda = re.search(patron, texto)
print(f"Se encuentra la palabra '{patron}' en el texto: {busqueda}")

patron = "ayuda"
for hallazgo in re.finditer(patron, texto):
    print(f"Se encuentra la palabra '{patron}' en el texto: {hallazgo.span()}")

texto = "Llamada al 752-555-0113 ya mismo"
print(f"\n\nTexto: {texto}\n\n")

patron = r"\d{3}-\d{3}-\d{4}"

busqueda = re.search(patron, texto)
print(f"Se encuentra el patrón '{patron}' en el texto: {bool(busqueda)}")
print(f"Hallazgo: {busqueda.group()}")

patron = re.compile(r"(\d{3})-(\d{3})-(\d{4})")

busqueda = patron.search(texto)
print(f"\nSe encuentra el patrón '{patron}' en el texto: {bool(busqueda)}")
print(f"Hallazgo: {busqueda.group()}")
print(f"Grupo 1: {busqueda.group(1)}")
print(f"Grupo 2: {busqueda.group(2)}")
print(f"Grupo 3: {busqueda.group(3)}")

print("\n\nValidar claves de acceso:")

clave = input("Ingrese una clave: ")

patron = r"\D{1}\w{7}"

busqueda = re.search(patron, clave)

if busqueda:
    print(f"Clave válida: {busqueda.group()}")
else:
    print("Clave inválida")
