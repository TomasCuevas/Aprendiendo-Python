"""
Los decoradores son patrones de diseño en Python utilizados
para dar nueva funcionalidad a objetos (funciones),
modificando su comportamiento sin alterar su estructura: son
funciones que modifican funciones.
"""

print("--------------------------------")
print("Sin decoradores\n")


def cambiar_letras(tipo):
    def mayuscula(texto):
        print(texto.upper())

    def minuscula(texto):
        print(texto.lower())

    if tipo == "may":
        return mayuscula
    elif tipo == "min":
        return minuscula


operacion = cambiar_letras("may")
operacion("palabra")


print("\n\n--------------------------------")
print("Utilizando decoradores")


def decorar_saludo(funcion):
    def saludo(palabra):
        print("\nHola")
        funcion(palabra)
        print("Adios")

    return saludo


@decorar_saludo
def mayuscula(texto):
    print(texto.upper())


@decorar_saludo
def minuscula(texto):
    print(texto.lower())


mayuscula("segundo metodo")
minuscula("SEGUNDO METODO")

print("\n\n--------------------------------")
print("Otra forma de usar decoradores")


def decorar_saludo(funcion):
    def saludo(palabra):
        print("\nHola")
        funcion(palabra)
        print("Adios")

    return saludo


def mayuscula(texto):
    print(texto.upper())


def minuscula(texto):
    print(texto.lower())


mayuscula_decorada = decorar_saludo(mayuscula)
minuscula_decorada = decorar_saludo(minuscula)

mayuscula_decorada("tercer metodo")
minuscula_decorada("TERCER METODO")
