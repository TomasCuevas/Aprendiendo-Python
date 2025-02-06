"""
Los generadores son tipos especiales de funciones que
devuelven un iterador que no almacena su contenido
completo en memoria, sino que "demora" la ejecución de una
expresión hasta que su valor se solicita.
"""

print("===============================")
print("Retornar un valor")
print("===============================\n")


def mi_funcion():
    return 4


def mi_generador():
    yield 4


print(mi_funcion())
print(mi_generador())

g = mi_generador()
print(next(g))


print("\n===============================")
print("Retornar una lista")
print("===============================\n")


def mi_funcion():
    lista = []
    for x in range(1, 5):
        lista.append(x * 10)

    return lista


def mi_generador():
    for x in range(1, 5):
        yield x * 10


print(mi_funcion())
print(mi_generador())

g = mi_generador()
print(next(g))
print(next(g))


print("\n===============================")
print("Un ejemplo más")
print("===============================\n")


def mi_generador():
    x = 1
    yield x
    x = 2
    yield x
    x = 3
    yield x


g = mi_generador()
print(g)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
