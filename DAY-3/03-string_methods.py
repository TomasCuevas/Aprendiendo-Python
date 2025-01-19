texto = 'Este es el texto de Tomás'
a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = " "

resultado = texto
print(f"Texto original: {resultado}")
print("\n")

resultado = texto.upper()
print(f"upper(): {resultado}")
print("\n")

resultado = texto[2].upper()
print(f"[2].upper(): {resultado}")
print("\n")

resultado = texto.lower()
print(f"lower(): {resultado}")
print("\n")

resultado = texto.split()
print(f"split(): {resultado}")
print("\n")

resultado = texto.split("t")
print(f"split('t'): {resultado}")
print("\n")

resultado = e.join([a, b, c, d])
print(f"join([a, b, c, d]): {resultado}")
print("\n")

resultado = texto.find("es")
print(f"find('es'): {resultado}")
print("\n")

resultado = texto.replace("Tomás", "Juan")
print(f"replace('Tomás', 'Juan'): {resultado}")
print("\n")