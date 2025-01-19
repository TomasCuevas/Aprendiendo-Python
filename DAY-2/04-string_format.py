x = 10
y = 5

print("Mis numeros son " + str(x) + " y " + str(y) + " (con STR)")
print("Mis numeros son {} y {} (con FORMAT)".format(x, y))
print(f"Mis numeros son {x} y {y} (con F-STRING)")
print("\n")

print("La suma de " + str(x) + " y " + str(y) + " es " + str(x + y) + " (con STR)")
print("La suma de {} y {} es {} (con FORMAT)".format(x, y, x + y))
print(f"La suma de {x} y {y} es {x + y} (con F-STRING)")
print("\n")

color = 'rojo'
matricula = 543216

print(f"El auto es {color} y su matricula es {matricula}")