frutas = ["banana", "manzana", "ciruela", "frutilla", "sandia"]
cadena = "Hola Tomás"
numeros = [2, 5, 8, 10]

# Evitando que se coma una frutilla con la sentencia (continue)
print("CONTINUE")

for fruta in frutas:
  if fruta == "frutilla":
    continue
  
  print(f"Me voy a comer una {fruta}")


# Evitar que el bucle siga ejecutandose
print("BREAK")

for fruta in frutas:
  if fruta == "ciruela":
    break
  
  print(f"Me voy a comer una {fruta}")

# Recorrer una cadena de texto
for letra in cadena:
  print(letra)

# For en una sola linea de codigo
numeros_duplicados = [x*2 for x in numeros] 
print(numeros_duplicados)
