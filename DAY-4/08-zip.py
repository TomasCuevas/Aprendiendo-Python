"""
    # ZIP(): 
        La función zip() crea un iterador formado por los elementos agrupados del mismo índice provenientes de dos o más iterables. 
        Zip deriva de zipper (cremallera o cierre), de modo que es una analogía muy útil para recordar.  
"""

nombres = ["Tomas", "Juan", "Maria"]
edades = [25, 30, 35]

combinados = list(zip(nombres, edades))
for nombre, edad in combinados:
  print(f"{nombre} tiene {edad} años")
  
print("\n")
ciudades = ["Buenos Aires", "Santiago", "Montevideo"]
combinados = list(zip(nombres, edades, ciudades))
for nombre, edad, ciudad in combinados:
  print(f"{nombre} tiene {edad} años y vive en {ciudad}")