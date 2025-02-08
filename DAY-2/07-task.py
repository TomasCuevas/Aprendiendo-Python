"""
    # TAREA: 
        La situación es esta: tú trabajas en una empresa donde los vendedores reciben comisiones
        del 13% por sus ventas totales, y tu jefe quiere que ayudes a los vendedores a calcular sus
        comisiones creando un programa que les pregunte su nombre y cuánto han vendido en este
        mes. Tu programa le va a responder con una frase que incluya su nombre y el monto que le
        corresponde por las comisiones.
"""


nombre = input("Por favor, escriba su nombre: ")
ventas = int(input("Escribe la cantidad de ventas: $"))
comision = round(ventas * 13 / 100, 2)

print(f"\nHola {nombre}, tus comisiones de este mes son ${comision}")