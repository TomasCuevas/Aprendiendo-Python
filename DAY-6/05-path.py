"""
    # La clase Path: 
        Permite representar rutas de archivos en el sistema de archivos de nuestro sistema operativo. 
        Se destaca por su legibilidad frente a alternativas semejantes.

    # Métodos y propiedades de Path:
        1. base = Path.home() --> Devuelve un objeto Path representando el directorio base del usuario
        2. ruta2 = ruta.with_name("LaPedrera.txt") --> Devuelve un nuevo objeto Path cambiando únicamente el nombre de archivo
        3. continente = ruta.parent.parent --> Cada invocación de la propiedad parentdevuelve la ruta de jerarquía inmediata superior
        4. print(continente) >> C:\Users\...\Europa
"""


from pathlib import Path

print("\n===== Path.home():")
base = Path.home()
guia = Path(base, "Europa", "España", Path("Barcelona", "Sagrada_Familia.txt"))
print(guia)

print("\n===== ruta.with_name('file'):")
guia2 = guia.with_name("LaPedrera.txt")
print(guia2)

print("\n===== ruta.parent.parent:")
pais = guia.parent.parent
print(pais)

print("\n===== Path('ruta').glob('*.txt'):")
guia = Path(Path.home(), "Europa")
for txt in Path(guia).glob("*.txt"):
    print(txt)

print("\n===== Path('ruta').glob('**/*.txt'):")
guia = Path(Path.home(), "Europa")
for txt in Path(guia).glob("**/*.txt"):
    print(txt)

print("\n===== relative_to('ruta'):")
guia = Path("Europa", "España", "Barcelona", "Sagrada_Familia.txt")
en_europa = guia.relative_to(Path("Europa"))
en_espana = guia.relative_to(Path("Europa", "España"))
print(en_europa)
print(en_espana)
