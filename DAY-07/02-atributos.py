"""
    # ATRIBUTOS: 
        Los atributos son variables que pertenecen a la clase. Existen atributos de clase (compartidos por todas las instancias de la clase),
        y de instancia (que son distintos en cada instancia de la clase).

        Todas las clases tienen una función que se ejecuta al instanciarla, llamada __init__() , y que se utiliza para asignar
        valores a las propiedades del objeto que está siendo creado.

        self: representa a la instancia del objeto que se va a crear
"""


class Pajaro:
    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie


mi_pajaro = Pajaro("rojo", "Tucán")
print(f"Mi pajaro es un {mi_pajaro.especie} y es de color {mi_pajaro.color}")
print(f"Mi pajaro tiene alas: {mi_pajaro.alas}")
