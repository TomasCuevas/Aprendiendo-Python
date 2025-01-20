# RANGE(): La función range( ) devuelve una secuencia de números dados 3 parámetros. Se utiliza fundamentalmente para 
# controlar el número de ejecuciones de un loop o para crear rápidamenteuna serie de valores.

for i in range(10):
  print(i)

print("\n")
for i in range(1, 11):
  print(i)

print("\n")
for i in range(1, 11, 2):
  print(i)
  
print("\n")
numeros = list(range(1, 11))
print(numeros)