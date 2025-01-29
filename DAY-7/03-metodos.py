# Metodos: Los objetos creados a partir de clases también contienen métodos. Dicho de otra manera,
# los métodos son funciones que pertenecen al objeto.

# Cada vez que un atributo del objeto sea invocado (por ejemplo, en una función), debe incluirse self,
# que refiere a la instancia en cuestión, indicando la pertenencia de este atributo.


class Pajaro:
    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print(f"Pio, pio, pio! Mi color es {self.color}")

    def volar(self, metros):
        print(f"El pajaro ha volado {metros} metros")


piolin = Pajaro("amarillo", "Canario")

piolin.piar()
piolin.volar(100)
