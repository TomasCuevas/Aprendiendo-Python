numeros = [4, 7, 1, 42, 55, 15]

# Encontrar el numero mayor de una lista
numero_mas_alto = max(numeros)
print(numero_mas_alto)

# Encontrar el numero menor de una lista
numero_mas_bajo = min(numeros)
print(numero_mas_bajo)

# Redondear a 6 decimales
numero = round(12.34567783455, 6)
print(numero)

# Retorna False -> 0, vacio, False, none / True -> distinto a 0, True, cadena, datos no vacios
resultado_bool = bool(15)
print(resultado_bool)

# Retorna True si todos los valores son verdaderos
resultado_all = all([234, "Buenas", [15, 4, 2000]])
print(resultado_all)

# Sumar todos los valores de un iterable
suma_total = sum(numeros)
print(suma_total)