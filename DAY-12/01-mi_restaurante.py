from tkinter import *


# iniciar tkinter
aplicacion = Tk()

# tamaño de la ventana
aplicacion.geometry("1020x630+480+270")

# evitar maximixar
aplicacion.resizable(False, False)

# titulo de la ventana
aplicacion.title("Mi Restaurante - Sistema de Facturación")

# color de fondo
aplicacion.configure(bg="burlywood")

# evitar que se cierre la aplicacion
aplicacion.mainloop()