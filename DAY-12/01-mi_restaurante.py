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

# panel superior
panel_superior = Frame(aplicacion, bd=1, relief=FLAT)
panel_superior.pack(side=TOP)

# etiqueta titulo
etiqueta_titulo = Label(panel_superior, text="Sistema de Facturación", fg="azure4", font=("Montserrat", 45), bg="burlywood")
etiqueta_titulo.grid(row=0, column=0)

# panel izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

# panel costos
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT)
panel_costos.pack(side=BOTTOM)

# panel comidas
panel_comidas = LabelFrame(panel_izquierdo, text="Comida", font=("Montserrat", 20, "bold"), bd=1, relief=FLAT, fg="azure4")
panel_comidas.pack(side=LEFT)

# panel bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text="Bebidas", font=("Montserrat", 20, "bold"), bd=1, relief=FLAT, fg="azure4")
panel_bebidas.pack(side=LEFT)

# panel postres
panel_postres = LabelFrame(panel_izquierdo, text="Postres", font=("Montserrat", 20, "bold"), bd=1, relief=FLAT, fg="azure4") 
panel_postres.pack(side=LEFT)

# panel derecha
panel_derecha = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecha.pack(side=RIGHT)

# panel calculadora
panel_calculadora = Frame(panel_derecha, bd=1, relief=FLAT, bg="burlywood")
panel_calculadora.pack()

# panel recibo
panel_recibo = Frame(panel_derecha, bd=1, relief=FLAT, bg="burlywood")
panel_recibo.pack()

# panel botones
panel_botones = Frame(panel_derecha, bd=1, relief=FLAT, bg="burlywood")
panel_botones.pack()

# evitar que se cierre la aplicacion
aplicacion.mainloop()