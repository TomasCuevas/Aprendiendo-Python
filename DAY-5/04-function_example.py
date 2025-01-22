precios_cafe = [("Capuchino", 1.5), ("Expreso", 2.2), ("Cafe", 1.2), ("Moka", 1.7)]  

def cafe_mas_caro(lista_precios):
  precio_mayor = 0
  cafe_mas_caro = ""
  
  for nombre, precio in lista_precios:
    if precio > precio_mayor:
      precio_mayor = precio
      cafe_mas_caro = nombre

  return (cafe_mas_caro, precio_mayor)

resultado = cafe_mas_caro(precios_cafe)
print(f"El café más caro es '{resultado[0]}' con un precio de {resultado[1]} euros") 