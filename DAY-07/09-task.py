"""
    # TAREA:
        Primero vas a crear una clase llamada Persona, y Persona va a tener solo dos atributos:
        nombre y apellido. Luego, vas a crear una segunda clase llamada Cliente, y Cliente va a
        heredar de Persona, porque los clientes son personas, por lo que el Cliente va a heredar
        entonces los atributos de Persona, pero también va a tener atributos propios, como número
        de cuenta y balance, es decir, el saldo que tiene en su cuenta bancaria.

        Pero eso no es todo: Cliente también va a tener tres métodos. El primero va a ser uno de los
        métodos especiales y es el que permite que podamos imprimir a nuestro cliente. Este método
        va a permitir que cuando el código pida imprimir Cliente, se muestren todos sus datos,
        incluyendo el balance de su cuenta. Luego, un método llamado Depositar, que le va a permitir
        decidir cuánto dinero quiere agregar a su cuenta. Y finalmente, un tercer método llamado
        Retirar, que le permita decidir cuánto dinero quiere sacar de su cuenta.

        Una vez que hayas creado estas dos clases, tienes que crear el código para que tu programa se
        desarrolle, pidiéndole al usuario que elija si quiere hacer depósitos o retiros. El usuario puede
        hacer tantas operaciones como quiera hasta que decida salir del programa. Por lo tanto, nuestro
        código tiene que ir llevando la cuenta de cuánto dinero hay en el balance, y debes procurar, por
        supuesto, que el cliente nunca pueda retirar más dinero del que posee. Esto no está permitido.
"""

from random import randint
from os import system


class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    def __init__(self, nombre, apellido, numero, balance=0):
        super().__init__(nombre, apellido)
        self.numero = numero
        self.balance = balance

    def depositar(self, cantidad):
        self.balance += cantidad
        print(f"Se ha depositado ${cantidad} al cliente {self.nombre} {self.apellido}")
        print(f"Su saldo ahora es ${self.balance}")

    def retirar(self, cantidad):
        if cantidad <= self.balance:
            self.balance -= cantidad
            print(f"Se ha retirado ${cantidad} del cliente {self.nombre} {self.apellido}")
            print(f"Su saldo ahora es ${self.balance}")
        else:
            print(f"No puede retirar ${cantidad}. Tu saldo es ${self.balance}")

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}, Numero de cuenta: {self.numero}, Saldo: ${self.balance}"


def continuar():
    """
    Se muestra un mensaje para continuar.
    """
    input("\n\n\nPulsa 'ENTER' para continuar...")


def crear_cliente():
    """
    Permite crear un cliente.
    """
    print("\n====== INGRESE SUS DATOS ====== \n\n")
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    cliente = Cliente(nombre, apellido, randint(1000, 9999))

    return cliente


def inicio():
    """
    Función principal. Permite que el usuario elija si quiere depositar dinero, retirar o salir.
    """
    cliente = crear_cliente()
    opcion_de_menu = 0

    while opcion_de_menu != 3:
        system("cls")

        print("\n====== MENU PRINCIPAL ======\n\n")
        print("[1] Depositar")
        print("[2] Retirar")
        print("[3] Salir")

        opcion = input("Elija una opción: ")
        system("cls")

        match (opcion):
            case "1":
                print("\n====== INGRESE EL IMPORTE ======\n\n")
                cantidad = int(input("Ingrese la cantidad a depositar: $"))
                cliente.depositar(cantidad)
                continuar()
            case "2":
                print("\n====== INGRESE EL IMPORTE ======\n\n")
                cantidad = int(input("Ingrese la cantidad a retirar: $"))
                cliente.retirar(cantidad)
                continuar()
            case "3":
                opcion_de_menu = 3


inicio()
