# Crear un conjunto con set()
conjunto = set(["dato1", "dato2"])
print(conjunto)

# Meter un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato1", "dato2"])
conjunto2 = {conjunto1, "dato3"}
print(conjunto2)

# Teoria de conjuntos
conjunto3 = {1,3,5,7}
conjunto4 = {1,3,7}

# Verificar si es un subconjunto
issubset_resultado = conjunto4.issubset(conjunto3)
print(issubset_resultado)

left_arrow_resultado = conjunto4 <= conjunto3
print(left_arrow_resultado)

# Verificar si es un superconjunto
issupersett_resultado = conjunto3.issuperset(conjunto4)
print(issupersett_resultado)

right_arrow_resultado = conjunto3 > conjunto4
print(right_arrow_resultado)

# Verificar si hay algun numero en comun (False si lo hay y True si no lo hay)
resultado = conjunto3.isdisjoint(conjunto4)
print(resultado)