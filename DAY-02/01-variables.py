"""
    # VARIABLES: 
        Las variables son espacios de memoria que almacenan valores o datos de distintos tipos, y (como su nombre indica) pueden variar. 
        Se crean en el momento que se les asigna un valor, por lo cual en Python no requerimos declararlas previamente.

        Existen convenciones y buenas prácticas asociadas al nombre de las variables creadas en Python. Las mismas tienen la intención de facilitar 
        la interpretabilidad y mantenimiento del código creado.

    #REGLAS:
        1. Legible: nombre de la variable es relevante según su contenido.
        2. Unidad: no existen espacios (puedes incorporar guiones bajos).
        3. Hispanismos: omitir signos específicos del idioma español,como tildes o la letra ñ.
        4. Nombres: los nombres de las variables no deben empezar por números (aunque pueden contenerlos al final).
        5. Signos/símbolos: no se deben incluir: " ' , < > / ? | \ ( ) ! @ #$ % ^ & * ~ - +.
        6. Palabras clave: no utilizamos palabras reservadas por Python
"""


nombre = 'Tomás'
print(nombre)

nombre = 'Laura'
print(nombre + '\n')

edad = 24
print(edad)

n1 = 200
n2 = 300
print(n1 + n2)

nombre_del_usuario = input('\nEscribe tu nombre: ')
print("Tu nombre es " + nombre_del_usuario + '\n')

frase_1 = 'Hola '
frase_2 = 'Mundo'
frase_3 = '!'
print(frase_1 + frase_2 + frase_3)