"""
    # EJERCICIO:
        Crear un paquete llamado "mi_paquete" con dos subpaquetes: "suma_y_resta" y "saludo".
        Dentro de "suma_y_resta" crear un archivo llamado "operaciones.py" con las funciones suma y resta.
        Dentro de "saludo" crear un archivo llamado "saludo.py" con la función saludar.
"""

from paquete import suma_y_resta
from paquete.subpaquete import saludo

suma_y_resta.suma(5, 3)
suma_y_resta.resta(5, 3)

saludo.saludar()
