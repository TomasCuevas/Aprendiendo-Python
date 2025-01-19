# CONVERSIONES: Python realiza conversiones implícitas de tipos de datos automáticamente para operar 
# con valores numéricos. En otros casos, necesitaremos generar una conversión de manera explícita. 

num1 = 20
num2 = 30.5

num1 = num1 + num2

print(type(num1))
print(type(num2))
print("\n")

num3 = 5.8
print(num3)
print(type(num3))
print("\n")

num4 = int(num3)
print(num4)
print(type(num4))
print("\n")

edad = input("Escribe tu edad: ")
edad = int(edad)
nueva_edad = edad + 1
print(edad)
print(nueva_edad)
print(type(edad))
print(type(nueva_edad))
