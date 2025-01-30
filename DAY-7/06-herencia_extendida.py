# Herencia extendida: Las clases "hijas" que heredan de las clases superiores, pueden crear nuevos métodos o sobrescribir los
# de la clase "padre". Asimismo, una clase "hija" puede heredar de una o más clases, y a su vez transmitir herencia a clases "nietas".

# Si varias superclases tienen los mismos atributos o métodos, la subclase sólo podrá heredar de una de ellas.
# En estos casos Python dará prioridad a la clase que se encuentre más a la izquierda.

# Del mismo modo, si un mismo método se hereda por parte de la clase "padre", e "hija", la clase "nieta" tendrá preferencia
# por aquella más próxima ascendente (siguiendo nuestro esquema, la tomará de la clase "hija").

# Un método dado se buscará primero en la propia clase, y de no hallarse, se explorará las superiores.


class Animal:
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(sef):
        print("Este animal ha nacido.")

    def hablar(self):
        print("Este animal emite un sonido.")


class Pajaro(Animal):
    def __init__(self, edad, color, altura_vuelo):
        super().__init__(edad, color)
        self.altura_vuelo = altura_vuelo

    def hablar(self):
        print("Pio, pio, pio!")

    def volar(self, metros):
        print(f"El pajaro ha volado {metros} metros")


piolin = Pajaro(2, "amarillo", 20)
mi_animal = Animal(2, "azul")

print("\n---Piolin---")
piolin.hablar()
piolin.volar(32)

print("\n---Mi animal---")
mi_animal.hablar()


class Padre:
    def hablar(self):
        print("Hola")


class Madre:
    def reir(self):
        print("Ja ja ja")

    def hablar(self):
        print("Que tal?")


class Hijo(Padre, Madre):
    pass


class Nieto(Hijo):
    pass


mi_nieto = Nieto()

print("\n---Mi nieto---")
print(Nieto.__mro__)
mi_nieto.hablar()
mi_nieto.reir()
