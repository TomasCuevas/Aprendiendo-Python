print("1. =============================================================\n")

# 1. Crea una función llamada devolver_distintos() que reciba 3 integers como parámetros.

# Si la suma de los 3 numeros es mayor a 15, va a devolver el número mayor.
# Si la suma de los 3 numeros es menor a 10, va a devolver el número menor .
# Si la suma de los 3 números es un valor entre 10 y 15 (incluidos) va a devolver el número de valor intermedio.


def devolver_distintos(num1, num2, num3):
    numeros = [num1, num2, num3]
    suma = sum(numeros)

    if suma > 15:
        return max(numeros)
    if suma < 10:
        return min(numeros)
    else:
        numeros.sort()
        return numeros[1]


print(devolver_distintos(16, 4, 43))  # MAYOR --> 43
print(devolver_distintos(3, 4, 2))  # MENOR --> 2
print(devolver_distintos(6, 2, 4))  # INTERMEDIO --> 4


print("\n2. =============================================================\n")

# 2. Escribe una función (puedes ponerle cualquier nombre que quieras) que reciba cualquier palabra como parámetro,
# y que devuelva todas sus letras únicas (sin repetir) pero en orden alfabético.

# Por ejemplo si al invocar esta función pasamos la palabra "entretenido", debería devolver ['d', 'e', 'i', 'n', 'o', 'r', 't']


def devolver_unicas(palabra):
    letras_unicas = list(set(palabra.lower()))
    letras_unicas.sort()
    return letras_unicas


print(devolver_unicas("Psicoloogiaa"))  # ['a', 'c', 'g', 'i', 'l', 'o', 'p', 's']


print("\n3. =============================================================\n")

# 3. Escribe una función que requiera una cantidad indefinida de argumentos. Lo que hará esta función es devolver True si en algún momento
# se ha ingresado al numero cero repetido dos veces consecutivas .

# (5,6,1,0,0,9,3,5) --> True
# (6,0,5,1,0,3,0,1) --> False


def ceros_vecinos(*args):
    for index, arg in enumerate(args):
        if arg == 0 and args[index - 1] == 0:
            return True

    return False


print(ceros_vecinos(5, 6, 1, 0, 0, 9, 3, 5))  # True
print(ceros_vecinos(6, 0, 5, 1, 0, 3, 0, 1))  # False

print("\n4. =============================================================\n")

# 4. Escribe una función llamada contar_primos() que requiera un solo argumento numérico.

# Esta función va a mostrar en pantalla todos los números primos existentes en el rango que va desde cero hasta ese número incluido,
# y va a devolver la cantidad de números primos que encontró.

# Aclaración, por convención el 0 y el 1 no se consideran primos.


def contar_primos(numero):
    numeros_primos = []

    for numero in range(2, numero + 1):
        if numero > 1:
            for i in range(2, int(numero**0.5) + 1):
                if numero % i == 0:
                    break
            else:
                numeros_primos.append(numero)

    print(f"Los numeros primos entra 2 y {numero} son: {numeros_primos}")
    return len(numeros_primos)


print(f"\nLa cantidad de numeros primos son: {contar_primos(398)}")
