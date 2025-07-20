"""
    El módulo datetime (incorporado en Python) puede importarse en
    proyectos para trabajar con fechas y horas, así como intervalos y
    duraciones.

    # fecha:
        año,mes,día son integers comprendidos en los rangos de fechas "reales" (12 meses y 31 días
        como máximo). También podemos extraer el año, mes y día individualmente:

    # hora:
        Los argumentos son opcionales (se asumen 0 si no se indican), y deben estar comprendidos
        entre 0 y 24 para las horas, 0 y 60 para minutos y segundos, y 0 y 1000000 para los microsegundos.
"""

from datetime import datetime, date, time

mi_hora = time(17, 35)
print(type(mi_hora))

print(f"\nHora exacta: {mi_hora}")
print(f"Hora: {mi_hora.hour}")
print(f"Minuto: {mi_hora.minute}")

mi_dia = date(2025, 2, 8)
print(f"\nFecha: {mi_dia}")
print(f"Año: {mi_dia.year}")
print(f"Mes: {mi_dia.month}")
print(f"Día: {mi_dia.day}")
print(f"Otra forma de mostrar la fecha: {mi_dia.ctime()}")
print(f"Reemplazando el mes: {mi_dia.replace(month=7)}")

print(f"\nFecha y hora actual: {datetime.now()}")

nacimiento = date(1990, 3, 5)
defuncion = date(2064, 2, 8)
vida = defuncion - nacimiento

print(f"\nMurio a los {vida.days // 365} años")
print(f"Vivio la cantidad de {vida.days} dias")

despierta = datetime(2022, 10, 5, 7, 30)
duerme = datetime(2022, 10, 5, 23, 0)
vigilia = duerme - despierta

print(f"\nEstuvo despierto {vigilia.seconds} segundos")

