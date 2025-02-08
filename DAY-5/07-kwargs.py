"""
    # KWARGS: 
        Los argumentos con palabras clave (keyword arguments, abreviado kwargs), sirven para identificar el argumento por su nombre, independientemente
        de la posición en la que se pasen a su función. 
        Si no se conoce de antemano su cantidad, se utiliza el parámetro **kwargs que los agrupa en un diccionario.

    # Al igual que para *args, el nombre **kwargs no es mandatorio pero si es sugerido como buena práctica. 
    # Cualquier nombre iniciado en ** referirá a estos argumentos de cantidad variable.
"""


def suma(**kwargs):
    total = 0

    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")
        total += valor

    return total


print(suma(a=1, b=2, c=3, d=4, e=5))


def prueba(num1, num2, *args, **kwargs):
    print("\n")
    print(f"El primer valor es {num1}")
    print(f"El segundo valor es {num2}")

    for arg in args:
        print(f"arg =  {arg}")

    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")


args = [100, 200, 300]
kwargs = {"a": 1, "b": 2, "c": 3}

prueba(1, 2, *args, **kwargs)
