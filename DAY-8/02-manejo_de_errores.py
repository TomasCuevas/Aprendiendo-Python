# Manejo de Errores: Existen estrategias para capturar y gestionar los errores que pueden presentarse al ejecutar un programa,
# a fines de evitar una falla mayor y controlar la información que es mostrada al usuario.

# TRY: El código que se encuentra dentro de try se ejecuta hasta finalizar o hasta que se presenta un error(excepción)
# EXCEPT: Contiene el manejador de errores (respuesta del programa ante un error), atrapando las excepciones que se presentan durante la ejecución de try
# ELSE: Engloba el código que se ejecutará únicamente cuando ninguna excepción haya sido detectada en la ejecución de try ( sin errores )
# FINALLY: Contiene código que se ejecuta siempre, se hayan presentado o no errores.


def suma():
    n1 = int(input("Introduce el primer numero: "))
    n2 = int(input("Introduce el segundo numero: "))
    print(n1 + n2)


try:
    suma()
except TypeError:
    print("Error: Estas intentando sumar dos numeros de diferentes tipos")
except ValueError:
    print("Error: El numero que ingresaste no es un numero")
else:
    print("Todo bien")
finally:
    print("Finalizado")


def pedir_numero():
    while True:
        try:
            numero = int(input("Introduce un numero: "))
        except:
            print("Error: El numero ingresado no es un numero")
        else:
            print(f"Ingresaste el numero {numero}")
            break

    print("Gracias")


pedir_numero()
