# Puedes encontrarlos con el nombre de métodos mágicos o dunder methods (del inglés: dunder = double underscore , o doble guión bajo).
# Pueden ayudarnos a sobrescribir métodos incorporados de Python sobre nuestras clases para controlar el resultado devuelto.


class CD:
    def __init__(self, artista, titulo, canciones):
        self.artista = artista
        self.titulo = titulo
        self.canciones = canciones

    def __str__(self):
        return f"Album: {self.titulo} de {self.artista}"

    def __len__(self):
        return self.canciones

    def __del__(self):
        print("Se ha eliminado el CD exitosamente.")


mi_cd = CD("Led Zeppelin", "Led Zeppelin IV", 8)
print(mi_cd)
print(len(mi_cd))
del mi_cd
