# FUNCIONES DINAMICAS: La integración de diferentes herramientas de control de flujo, nos permite crear funciones dinámicas y flexibles. 
# Si debemos utilizarlas varias veces, lograremos un programa más limpio y sencillo de mantener, evitando repeticiones de código. 

def chequear_3_cifras(numero):
  return numero in range(100, 1000)

resultado = chequear_3_cifras(623)
print(f"El numero 623 tiene 3 cifras: {resultado}")

def chequear_3_cifras_en_lista(numeros):
  for numero in numeros:
    if numero in range(100, 1000):
      return True
    else:
      pass
  
  return False

numeros = [55, 398, 4560, 83]
resultado = chequear_3_cifras_en_lista(numeros)
print(f"\nEn la lista {numeros}, hay algun numero con 3 cifras: {resultado}")

def chequear_3_cifras_y_devolver(numeros):
  lista_de_numeros_con_3_cifras = []

  for numero in numeros:
    if numero in range(100, 1000):
      lista_de_numeros_con_3_cifras.append(numero)
      
  return lista_de_numeros_con_3_cifras

numeros = [55, 398, 4560, 823]
resultado = chequear_3_cifras_y_devolver(numeros)
print(f"\nDe la lista {numeros}, se han encontrado los siguientes numeros con 3 cifras: {resultado}")