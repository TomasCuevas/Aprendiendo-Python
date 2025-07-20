"""
    # FUNCIONES: 
        Una función es un bloque de código que solamente se ejecuta cuando es llamada. 
        Puede recibir información (en forma de parámetros), y devolver datos una vez procesados como resultado. 
"""

def saludar_persona():
  print("Ejecutando la función 'saludar_persona'")
  print("Hola")

saludar_persona()

def saludar_persona_con_nombre(nombre):
  print("\nEjecutando la función 'saludar_persona_con_nombre'")
  print(f"Hola {nombre}")

saludar_persona_con_nombre("Juan")