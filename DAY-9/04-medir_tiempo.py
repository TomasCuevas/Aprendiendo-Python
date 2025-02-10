"""
    MEDIR EL TIEMPO:
        Estudiar el tiempo transcurrido durante la ejecución de un
        código nos permite conocerlo mejor y tomar decisiones acerca
        de la vía más eficiete para resolver un problema. Tenemos dos
        módulos que nos ayudarán: time y timeit.

        # time:
            Mide el tiempo transcurrido entre dos puntos del código.
            Tiene dos funciones:
                - time(): devuelve el tiempo en segundos desde el 1 de enero de 1970.
                - sleep(): hace una pausa en segundos.

        # timeit:
            Mide el tiempo transcurrido entre dos puntos del código.
            Tiene dos funciones:
                - timeit(): devuelve el tiempo en segundos desde el 1 de enero de 1970.
                - sleep(): hace una pausa en segundos.
"""


import time
import timeit

def prueba_for(numero):
    lista = []
    for numero in range(1, numero + 1):
        lista.append(numero)
    
    return lista

def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1

    return lista


print("=====MEDICIONES CON TIME=====")

inicio = time.time()
prueba_for(1000)
final = time.time()

print(f"Tiempo transcurrido para el FOR medido con time: {final - inicio} segundos")


inicio = time.time()
prueba_while(1000)
final = time.time()

print(f"Tiempo transcurrido para el WHILE medido con time: {final - inicio} segundos")

print("\n\n=====MEDICIONES CON TIMEIT=====")

declaracion = """
prueba_for(1000)
"""

mi_setup = """
def prueba_for(numero):
    lista = []
    for numero in range(1, numero + 1):
        lista.append(numero)

    return lista
"""

duracion = timeit.timeit(declaracion, mi_setup, number=100000)
print(f"Tiempo transcurrido para el FOR medido con timeit: {duracion} segundos")

declaracion_2 = """
prueba_while(1000)
"""

mi_setup_2 = """
def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1   
"""

duracion_2 = timeit.timeit(declaracion_2, mi_setup_2, number=100000)
print(f"Tiempo transcurrido para el WHILE medido con timeit: {duracion_2} segundos")

