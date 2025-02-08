"""
    # Polimorfismo: 
        El polimorfismo es el pilar de la POO mediante el cual un mismo método puede comportarse de diferentes maneras
        según el objeto sobre el cual esté actuando, en función de cómo dicho método ha sido creado para la clase en particular.

    # El método len(): 
        Funciona en distintos tipos de objetos: listas, tuplas, strings, entreotros. Esto se debe a que
        para Python, lo importante no son los tipos de objetos, sino lo que pueden hacer: sus métodos.
"""


class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(f"Mi vaca {self.nombre} dice: ¡Muuuuuu!")


class Oveja:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(f"Mi oveja {self.nombre} dice: Beeeeee!")


vaca1 = Vaca("Pepona")
oveja1 = Oveja("Caracola")

print("\n---Vaca---")
vaca1.hablar()

print("\n---Oveja---")
oveja1.hablar()

print("\n---Animales utilizando for---")
animales = [vaca1, oveja1]

for animal in animales:
    animal.hablar()

print("\n---Animales utilizando una funcion especifica---")


def animal_hablar(animal):
    animal.hablar()


animal_hablar(vaca1)
animal_hablar(oveja1)
