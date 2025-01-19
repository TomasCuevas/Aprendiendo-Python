# La consigna es la siguiente: vas a crear un programa que primero le pida al usuario que
# ingrese un texto. Puede ser un texto cualquiera: un artículo entero, un párrafo, una frase, un
# poema, lo que quiera. Luego, el programa le va a pedir al usuario que también ingrese tres
# letras a su elección y a partir de ese momento nuestro código va a procesar esa información
# para hacer cinco tipos de análisis y devolverle al usuario la siguiente información:

# Primero: ¿cuántas veces aparece cada una de las letras que eligió?
# Segundo: le vas a decir al usuario cuántas palabras hay a lo largo de todo el texto.
# Tercero: nos va a informar cuál es la primera letra del texto y cuál es la última.
# Cuarto: el sistema nos va a mostrar cómo quedaría el texto si invirtiéramos el orden de las palabras.
# Y por último: el sistema nos va a decir si la palabra “Python” se encuentra dentro del texto.


print("=================================================================")
texto_ingresado = input("Ingrese un texto: ").lower()
primera_letra, segunda_letra, tercera_letra = input("Ingrese tres letras a su elección separadas por un espacio: ").lower().split(" ")

print("\n1. =================================================================")
contador_primera_letra = texto_ingresado.count(primera_letra)
contador_segunda_letra = texto_ingresado.count(segunda_letra)
contador_tercera_letra = texto_ingresado.count(tercera_letra)

print(f"La letra '{primera_letra}' aparece {contador_primera_letra} veces en el texto ingresado.")
print(f"La letra '{segunda_letra}' aparece {contador_segunda_letra} veces en el texto ingresado.")
print(f"La letra '{tercera_letra}' aparece {contador_tercera_letra} veces en el texto ingresado.")

print("\n2. =================================================================")
cuantas_palabras_hay = len(texto_ingresado.split(" "))

print(f"El texto ingresado tiene {cuantas_palabras_hay} palabras.")

print("\n3. =================================================================")
primera_letra_del_texto, ultima_letra_del_texto = [texto_ingresado[0], texto_ingresado[-1]]

print(f"La primera letra del texto es '{primera_letra_del_texto}' y la última letra es '{ultima_letra_del_texto}'.") 

print("\n4. =================================================================")
texto_invertido = texto_ingresado.split(" ")
texto_invertido.reverse()
texto_invertido = " ".join(texto_invertido)

print(f"El texto ingresado de forma invertida es: '{texto_invertido}'.")

print("\n5. =================================================================")
existe_la_palabra_python = texto_ingresado.find("python") != -1
dic = {True: "SÍ", False: "NO"}

print(f"La palabra 'Python' {dic[existe_la_palabra_python]} se encuentra en el texto ingresado.")