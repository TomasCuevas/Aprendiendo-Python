"""
    # TAREA: 
        La consigna es esta: el programa le va a preguntar al usuario su nombre, y luego le va a decir
        algo así como “Bueno, Juan, he pensado un número entre 1 y 100, y tienes solo ocho intentos
        para adivinar cuál crees que es el número”. Entonces, en cada intento el jugador dirá un
        número y el programa puede responder cuatro cosas distintas:

        1. Si el número que dijo el usuario es menor a 1 o superior a 100, le va a decir que ha elegido un número que no está permitido.
        2. Si el número que ha elegido el usuario es menor al que ha pensado el programa, le va a decir que su respuesta es incorrecta y que ha elegido un número menor al número secreto.
        3. Si el usuario eligió un número mayor al número secreto, también se lo hará saber de la misma manera.
        4. Y si el usuario acertó el número secreto, se le va a informar que ha ganado y cuántos intentos le ha tomado.
        5. Si el usuario no ha acertado en este primer intento, se le va a volver a pedir que elija otro número. Y así hasta que gane o hasta que se agoten los ocho intentos.
"""

from random import randint

numero_secreto = randint(1, 101)
acertado = False
nombre_del_usuario = input("¿Cuál es tu nombre? ")
print(f"\nBueno, {nombre_del_usuario}, he pensado un número entre 1 y 100, y tienes solo ocho intentos para adivinar cuál crees que es el número.")

intentos = 0
while intentos < 8:
  numero_del_usuario = int(input("\nDime un número: "))
  
  if numero_del_usuario < 1 or numero_del_usuario > 100:
    print("No es un número válido")
  elif numero_del_usuario == numero_secreto:
    print(f"¡Ganaste! ¡Has acertado en {intentos + 1} intento!")
    acertado = True
    break
  elif numero_del_usuario < numero_secreto:
    print("No es el número correcto. El número que eligió es MENOR al número secreto.")
  elif numero_del_usuario > numero_secreto:
    print("No es el número correcto. El número que eligió es MAYOR al número secreto.")
  
  intentos += 1

if not acertado:
  print(f"\nHas PERDIDO, no has sido capaz de adivinar el número secreto. El numero secreto era {numero_secreto}")