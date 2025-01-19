# REDONDEO: El redondeo facilita la interpretación de los valores calculados al limitar la cantidad 
# de decimales que se muestran en pantalla. También, nos permite aproximar valores decimales al entero más próximo. 

resultado = 90/7
redondeo = round(resultado)
print(redondeo)
print("\n")

valor = 95.7745354343
print(round(valor, 2))
print(round(valor, 4))
print(type(valor))
print(type(round(valor)))