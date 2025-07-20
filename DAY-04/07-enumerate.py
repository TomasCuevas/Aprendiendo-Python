"""
    # ENUMERATE(): 
        La función enumerate( ) nos facilita llevar la cuenta de las iteraciones, a través de un contador de índices
        de un iterable,que se puede utilizar de manera directa en un loop, o convertirse en una lista de tuplas con el método list( ).
"""

lista = ["a" , "b", "c"]
indice = 0

for elemento in lista:
  print(indice, elemento)
  indice += 1
  
print("\n")
for elemento in enumerate(lista):
  print(elemento)
  
print("\n")
for indice, elemento in enumerate(lista):
  print(f"indice: {indice}, elemento: {elemento}")
  
print("\n")
for elemento in enumerate(range(50, 56)):
  print(elemento)
  
print("\n")
mis_tuples = list(enumerate(lista))
print(mis_tuples)