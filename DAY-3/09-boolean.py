# BOOLEANS: Los booleanos son tipos de datos binarios (True/False), que surgen de operaciones lógicas, o pueden declararse explícitamente.

# OPERADORES LÓGICOS

# IGUAL A (==)
# DIFERENTE A ==
# MAYOR QUE>
# MENOR QUE <
# MAYOR O IGUAL QUE >=
# MENOR O IGUAL QUE <=

# and (Y) (Si ambas declaraciones son True)
# or (O) (Si al menos una declaración es True)
# not (NO) (Invierte el valor del booleano)

var1 = True

print(f"var1 es: {var1}")
print(f"El tipo de var1 es: {type(var1)}")
print("\n")

resultado = 5 > 2 + 3
print(f"5 es mayor que 2 + 3: {resultado}")
print("\n")

resultado = 5 == 2 + 3
print(f"5 es igual que 2 + 3: {resultado}")
print("\n")

resultado = 5 >= 2 + 3
print(f"5 es mayor o igual que 2 + 3: {resultado}")
print("\n")

resultado = 5 != 2 + 3
print(f"5 es diferente a 2 + 3: {resultado}")
print("\n")

resultado = bool(5 > 6)
print(f"5 es mayor que 6: {resultado}")
print("\n")

lista = [1, 2, 3, 4, 5]
resultado = 8 in lista
print(f"La lista es: {lista}")
print(f"8 esta en la lista: {resultado}")