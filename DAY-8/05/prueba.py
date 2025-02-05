"""
Unit Testing es un método o herramienta utilizado en programación
para determinar si un módulo o un conjunto de módulos de código
funciona correctamente. Dicha evaluación se realiza en un archivo
independiente. En Python, se implementa desde el módulo
incorporado unittest.
"""

import unittest
import cambia_texto


class ProbarCambiaTexto(unittest.TestCase):
    def test_mayusculas(self):
        palabra = "buenos dias"
        resultado = cambia_texto.todo_mayusculas(palabra)
        self.assertEqual(resultado, "BUENOS DIAS")


if __name__ == "__main__":
    unittest.main()
