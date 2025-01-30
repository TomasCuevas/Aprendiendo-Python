# La herencia es el proceso mediante el cual una clase puede tomar métodos y atributos de una clase superior, evitando repetición
# del código cuando varias clases tienen atributos o métodos en común.

# Es posible crear una clase "hija" con tan solo pasar como parámetro la clase de la que queremos heredar.
# Una clase "hija" puede sobreescribir los métodos o atributos, así como definir nuevos, que sean específicos para esta clase.


class Animal:
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(sef):
        print("Este animal ha nacido.")


class Pajaro(Animal):
    pass


piolin = Pajaro(2, "amarillo")
piolin.nacer()
print(piolin.color)
