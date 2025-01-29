# Tipos de metodos:

# Metodos de instancia: Poseen acceso a los atributos y metodos de la clase y de la instancia. Requieren una instancia de la clase.
# Metodos de clase: Poseen acceso a los atributos y metodos de la clase, pero no a los de la instancia. No requieren una instancia de la clase.
# Metodos estáticos: No poseen acceso a los atributos y metodos de la clase ni de la instancia. No requieren una instancia de la clase.

# Los métodos estáticos y de clase anteponen un decorador específico, que indica a Python el tipo de método que se estará definiendo.

# Así como los métodos de instancia requieren del parámetro self para acceder adicha instancia, los métodos de clase
# requieren del parámetro cls para acceder a los atributos de clase. Los métodos estáticos, dado que no pueden acceder a la
# instancia ni a la clase, no indican un parámetro semejante.


class Pajaro:
    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print("Pio, pio, pio!")

    def volar(self, metros):
        print(f"El pajaro ha volado {metros} metros")
        self.piar()

    def pintar_negro(self):
        self.color = "negro"
        print(f"Ahora el pajaro es de color {self.color}")

    @classmethod
    def poner_huevos(cls, cantidad):
        cls.alas = False

        print(f"Puso {cantidad} huevos")
        print(f"Ahora las alas son: {cls.alas}")

    @staticmethod
    def mirar():
        print("El pajaro mira")


piolin = Pajaro("amarillo", "Canario")

print("\n---Probando los métodos de instancia---")
piolin.pintar_negro()
piolin.volar(50)

print("\n---Probando los métodos de clase---")
Pajaro.poner_huevos(3)

print("\n---Probando los métodos estáticos---")
Pajaro.mirar()
