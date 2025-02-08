"""
    # CONTROL DE FLUJO: 
        El control de flujo determina el orden en que el código de un programa se va ejecutando. 
        En Python, el flujo está controlado por estructuras condicionales, loops y funciones.
"""


if 10 > 9:
  print("10 > 9: Es correcto \n")
  
if 5 == 2:
  print("5 == 2: Es correcto\n")
else:
  print("5 == 2: Es incorrecto\n")
  

mascota = "perro"

if mascota == "gato":
  print("Tienes un gato\n")
elif mascota == "perro":
  print("Tienes un perro\n")
else:
  print("No se que mascota tienes\n")

edad = 24
calificacion = 9

if edad >= 18:
  print("Eres mayor de edad")
  if calificacion >= 6:
    print("Estas aprobado\n")
  else:
    print("No has aprobado\n")
    
else:
  print("Eres menor de edad\n")