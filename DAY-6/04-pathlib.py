"""
    # El módulo pathlib: 
        Disponible desde Python 3.4, permite crear objetos Path, generando rutas que pueden ser interpretadas
        por diferentes sistemas operativos y cuentan con una serie de propiedades útiles.

        ruta = Path("C:/Users/Usuario/Desktop")

        A partir de una semántica sencilla, devuelve una ruta que el sistema puede comprender.
        Por ejemplo, en Windows, devolverá: C:\Users\Usuario\Desktop y en Mac: C:/Users/Usuario/Desktop

        Es posible concatenar objetos Path y strings con el delimitador "/" para construir rutas completas.
        ruta = Path("C:/Users/Usuario/Desktop") / "archivo.txt"

        Algunos métodos y propiedades sobre objetos Path:
            1. read_text(): lee el contenido del archivo sin necesidad de abrirlo y cerrarlo
            2. name: devuelve el nombre y extensión del archivo
            3. suffix: devuelve la extensión del archivo (sufijo)
            4. stem: devuelve el nombre del archivo sin su extensión (sufijo)
            5. exists(): verifica si el directorio o archivo al que referencia el objeto Path existe y devuelveun booleano de acuerdo al resultado (True/False)
"""


from pathlib import Path, PureWindowsPath

carpeta = Path(
    "C:/Users/Tomas/workspace/guia-cursos/Aprendiendo-Python/DAY-6/prueba.txt"
)

ruta_windows = PureWindowsPath(
    "C:/Users/Tomas/workspace/guia-cursos/Aprendiendo-Python/DAY-6/prueba.txt"
)

print("\n===== Path('ruta').read_text():")
print(carpeta.read_text())

print("\n===== Path('ruta').name:")
print(carpeta.name)

print("\n===== Path('ruta').suffix:")
print(carpeta.suffix)

print("\n===== Path('ruta').stem:")
print(carpeta.stem)

print("\n===== Path('ruta').exists():")
print(carpeta.exists())

print("\n===== PureWindowsPath('ruta'):")
print(ruta_windows)
