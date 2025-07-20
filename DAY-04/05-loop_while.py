"""
    # LOOP WHILE: 
        Si bien los loops while son otro tipo de bucles, resultan más parecidos a los condicionales if que a los loops for. 
        Podemos pensar a los loops while como una estructura condicional que se ejecuta en repetición, hasta que se convierte en falsa.

    # CONCEPTOS
        # BREAK: Si el código llega a una instrucción break, se produce la salida del bucle.
        # CONTINUE: La instrucción continue interrumpe la iteración actual dentro del bucle, llevando al programa a la parte superior del bucle.
        # PASS: La instrucción pass no altera el programa, ocupa un lugar donde se espera una declaración, pero no se desea realizar una acción. 
"""


monedas = 5 

while monedas > 0:
  print(f"Hay {monedas} monedas")
  monedas -= 1

print("\n")
respuesta = 's'
while respuesta == 's':
  respuesta = input("Quieres jugar otra vez? (s/n): ")
else:
  print("Gracias!")
  
print("\n")
nombre = input("Ingresa tu nombre: ")
for letra in nombre:
  if letra == 'a':
    break
  
  print(f"Letra: {letra}")
  
print("\n")
for letra in nombre:
  if letra == 'a':
    continue
  
  print(f"Letra: {letra}")