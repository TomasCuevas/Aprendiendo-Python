# El programa va a elegir una palabra secreta y le va a mostrar al jugador solamente una serie
# de guiones que representa la cantidad de letras que tiene la palabra. El jugador en cada turno
# deberá elegir una letra y si la letra se encuentra en la palabra oculta, el sistema le va a
# mostrar en qué lugares se encuentra. Pero si el jugador dice una letra que no se encuentra en
# la palabra oculta, pierde una vida.

# 1. Primero vas a crear un código que importe el método choice, ya que lo vas a necesitar
# para que el sistema pueda elegir una palabra al azar dentro de una lista de palabras que
# también vas a crear al comienzo.

# 2. Luego de eso, vas a crear tantas funciones como creas necesarias para que el programa
# haga cosas como pedirle al usuario que elija una letra, para corroborar si lo que el usuario
# ha ingresado es una letra válida, para chequear si la letra ingresada se encuentra en la
# palabra o no, para verificar si ha ganado o no, etc.

# 3. Recuerda escribir primero las funciones y luego el código que las implementa
# ordenadamente.

from random import choice


def generar_palabra_al_azar():
    lista_de_palabras = [
        "psicologia",
        "entretenido",
        "futbol",
        "matematicas",
        "programacion",
        "python",
        "astronauta",
        "celular",
        "editor",
        "continente",
        "planeta",
    ]

    return choice(lista_de_palabras)


def generar_palabra_oculta(palabra, letras_seleccionadas):
    palabra_oculta = ""

    for letra in palabra:
        if letra in letras_seleccionadas:
            palabra_oculta = palabra_oculta + letra
        else:
            palabra_oculta += "_"

    return palabra_oculta.capitalize()


def pedir_letra(letras_seleccionadas):
    letra = input("Escribe una letra: ").lower()
    abecedario = "abcdefghijklmnopqrstuvwxyz"

    while letra in letras_seleccionadas or letra not in abecedario:
        if letra not in abecedario:
            letra = input("Solo puedes ingresa una letra. Escribe otra: ").lower()
            continue

        if letra in letras_seleccionadas:
            letra = input(
                "La letra seleccionada ya ha sido elegida. Escribe otra: "
            ).lower()
            continue

    return letra.lower()


def verificar_letra(letra, palabra):
    if letra in palabra:
        return True
    else:
        return False


def verificar_si_gana(letras_seleccionadas, palabra):
    palabra_representada = generar_palabra_oculta(palabra, letras_seleccionadas)
    if palabra_representada.find("_") == -1:
        return True
    else:
        return False


def main():
    palabra = generar_palabra_al_azar()
    palabra_representada = generar_palabra_oculta(palabra, [])
    letras_seleccionadas = []
    intentos = 0
    MAXIMO_INTENTOS = len(set(palabra)) + 1
    gano = False

    print(
        f"\nBienvenido usuario. En este juego tienes que adivinar la palabra secreta. Tienes {MAXIMO_INTENTOS} intentos y en cada intento puedes elegir una letra de la palabra secreta.\n"
    )

    while intentos < MAXIMO_INTENTOS and not gano:
        print(f"\nPalabra a adivinar: {palabra_representada}\n")
        letra = pedir_letra(letras_seleccionadas).lower()
        letras_seleccionadas.append(letra)
        palabra_representada = generar_palabra_oculta(palabra, letras_seleccionadas)

        if not verificar_letra(letra, palabra):
            intentos += 1

        print(f"Te quedan {MAXIMO_INTENTOS - intentos} intentos")

        if verificar_si_gana(letras_seleccionadas, palabra):
            print("\n================================\n")
            print(
                f"¡Ganaste! Te tomo {intentos} intentos. La palabra era '{palabra.capitalize()}'"
            )
            gano = True
            break

    if not gano:
        print("\n================================\n")
        print(f"Has perdido. La palabra era '{palabra.capitalize()}'")


main()
