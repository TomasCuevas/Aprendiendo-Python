"""
    # TAREA:
        Vas a crear el tunero para una farmacia que tiene tres áreas de atención:
        perfumería, farmacia (que es donde venden los medicamentos), y cosméticos. Tu programa le
        tiene que preguntar al cliente a cuál de las áreas desea dirigirse, y le va a dar un número de
        turno según a qué área se dirija. Por ejemplo, si elige cosmética le va a dar el número C-54
        (“C” de cosmética). Luego de eso, nos va a preguntar si queremos sacar otro turno. Esto, en
        realidad, es para simular si viene un nuevo cliente. Y repetirá todo el proceso.

        Algunas cosas a tener en cuenta:
        
        Los diferentes clientes van a ir sacando turnos para diferentes áreas (perfumería, farmacia,
        cosmética), en diferentes órdenes, por lo que el sistema debe llevar la cuenta de cuántos turnos
        ha dado para cada una de esas áreas, y producir el siguiente número de cada área a medida
        que se lo pida. ¿No te parece genial aprovechar la eficiencia de los generadores para poder
        hacer esto?

        Por otro lado, el mensaje donde le comunicamos el número de espera al cliente, debería tener
        algo de texto adicional antes y después del número. Por ejemplo, “su turno es (-el número de
        turno con el del comienzo-)”, y luego algo así como “aguarde y será atendido”. Para que
        nuestro código no se repita, en vez de poner ese texto en cada una de las funciones que calculen
        los números, podemos aprovechar la flexibilidad de los decoradores para crear ese texto
        adicional una sola vez, y luego envolver a cualquiera de nuestras funciones con ese texto único.
"""


from os import system
from numeros import (
    generar_turno_perfumeria,
    generar_turno_farmacia,
    generar_turno_cosmeticos,
    decorar_informacion_de_turno,
)


def principal():
    perfumeria = generar_turno_perfumeria()
    farmacia = generar_turno_farmacia()
    cosmeticos = generar_turno_cosmeticos()

    while True:
        system("clear")
        print("\n========================")
        print("Bienvenido a la farmacia")
        print("========================\n\n")

        print(
            "Para Perfumería, PULSE 1\nPara Farmacia, PULSE 2\nPara Cosméticos, PULSE 3"
        )

        try:
            opcion = input("\nIngrese el número de la opción que desea: ")
            ["1", "2", "3"].index(opcion)
        except ValueError as e:
            print(e)
            continue

        if opcion == "1":
            decorar_informacion_de_turno(next(perfumeria))
        elif opcion == "2":
            decorar_informacion_de_turno(next(farmacia))
        elif opcion == "3":
            decorar_informacion_de_turno(next(cosmeticos))

        input("\n\n¿Desea sacar otro turno? Presione Enter para continuar...")


if __name__ == "__main__":
    principal()
