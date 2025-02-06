from os import system


def generar_turno_perfumeria():
    turno = 1
    while True:
        yield f"P-{turno}"
        turno += 1


def generar_turno_farmacia():
    turno = 1
    while True:
        yield f"F-{turno}"
        turno += 1


def generar_turno_cosmeticos():
    turno = 1
    while True:
        yield f"C-{turno}"
        turno += 1


def decorar_informacion_de_turno(turno):
    system("clear")
    print(f"Su turno es:\n({turno})\nAguarde y será atendido")
