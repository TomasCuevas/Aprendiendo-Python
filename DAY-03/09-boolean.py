"""
    # BOOLEANS: 
        Los booleanos son tipos de datos binarios (True/False), que surgen de operaciones lógicas, o pueden declararse explícitamente.

    # OPERADORES LÓGICOS
        1. IGUAL A (==)
        2. DIFERENTE A ==
        3. MAYOR QUE>
        4. MENOR QUE <
        5. MAYOR O IGUAL QUE >=
        6. MENOR O IGUAL QUE <=
        
        1. and (Y) (Si ambas declaraciones son True)
        2. or (O) (Si al menos una declaración es True)
        3. not (NO) (Invierte el valor del booleano)
"""


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