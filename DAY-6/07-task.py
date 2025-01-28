# tu código le va a dar primero la bienvenida al usuario, le va a informar
# la ruta de acceso al directorio donde se encuentra nuestra carpeta de recetas, le va a informar
# cuántas recetas hay en total dentro de esa carpeta, y luego le va a pedir que elija una de
# estas opciones que tenemos aquí:

# 1. La opción 1 le va a preguntar qué categoría elige (carnes, ensaladas, etc.), y una vez que
# el usuario elija una, le va a preguntar qué receta quiere leer, y mostrar su contenido.

# 2. En la opción 2 también se le va a hacer elegir una categoría, pero luego le va a pedir que
# escriba el nombre y el contenido de la nueva receta que quiere crear, y el programa va
# a crear ese archivo en el lugar correcto.

# 3. La opción 3 le va a preguntar el nombre de la categoría que quiere crear y va a generar
# una carpeta nueva con ese nombre.

# 4. La opción 4, hará todo lo mismo que la opción uno, pero en vez de leer la receta, la va
# a eliminar

# 5. La opción 5, le va a preguntar qué categoría quiere eliminar

# 6. Finalmente, la opción 6 simplemente va a finalizar la ejecución del código.

import os
from pathlib import Path


def ruta_raiz():
    """
    Retorna el path donde se encuentra la carpeta raiz de la aplicación
    """
    return Path(Path.home(), "Recetas")


def bienvenida():
    """
    Muestra el mensaje de bienvenida que se da al usuario en la pantalla principal
    """
    os.system("cls")
    total_recetas = sum(1 for i in Path(ruta_raiz()).rglob("*.txt"))

    print("*" * 50)
    print("***** Bienvenido al administrador de recetas *****")
    print("*" * 50)
    print(f"\nLa ruta de acceso a la carpeta de recetas es: {ruta_raiz()}")
    print(f"Hay {total_recetas} recetas en total\n")


def listar_menu_principal():
    """
    Lista todas las opciones del menu principal de la aplicación
    """
    print("1. Leer receta")
    print("2. Crear receta")
    print("3. Crear categoria")
    print("4. Eliminar recetas")
    print("5. Eliminar categoria")
    print("6. Salir\n\n")


def todas_las_categorias():
    """
    Retorna todas las categorias existentes
    """
    return os.listdir(Path(ruta_raiz()))


def recetas_por_categoria(categoria):
    """
    Retorna todas las recetas de la categoria que se recibe como argumento.
    """
    return os.listdir(Path(ruta_raiz(), categoria))


def listar_todas_las_categorias():
    """
    Listar todas las categorias existentes
    """
    categorias = todas_las_categorias()

    for categoria in categorias:
        print(f"{categorias.index(categoria) + 1}. {categoria}")


def listar_recetas_por_categoria(categoria):
    """
    Listar todas las recetas de la categoria que se recibe como argumento.
    """
    recetas = recetas_por_categoria(categoria)

    for receta in recetas:
        print(f"{recetas.index(receta) + 1}. {receta.split('.')[0]}")


def eliminar_todas_las_recetas_por_categoria(categoria):
    """
    Se eliminan todas las recetas de la categoria que se recibe como argumento.
    """
    recetas = recetas_por_categoria(categoria)
    for receta in recetas:
        os.remove(Path(ruta_raiz(), categoria, receta))


def continuar():
    """
    Se muestra un mensaje para continuar.
    """
    input("\n\n\nPulsa 'ENTER' para continuar...")


def seleccionar_categoria():
    """
    Elige una categoria.
        1. Se pide al usuario que seleccione una categoria.
        2. Se retorna la categoria seleccionada.
    """
    os.system("cls")
    categorias = todas_las_categorias()
    opcion = "x"

    while not opcion.isnumeric() or int(opcion) not in range(1, len(categorias) + 1):
        os.system("cls")
        print("Selecciona una categoria: \n")
        listar_todas_las_categorias()

        opcion = input("\nOpción: ")

    return categorias[int(opcion) - 1]


def seleccionar_receta(categoria):
    """
    Elige una receta de la categoria seleccionada.
        1. Se pide al usuario que seleccione la categoria.
        2. Se pide al usuario que seleccione la receta.
        3. Se retorna la receta seleccionada.
    """
    os.system("cls")
    recetas = recetas_por_categoria(categoria)
    opcion = "x"

    if len(recetas) == 0:
        print("No hay ninguna receta para esta categoria.")
        return

    while not opcion.isnumeric() or int(opcion) not in range(1, len(recetas) + 1):
        os.system("cls")
        print("Selecciona una receta: \n")
        listar_recetas_por_categoria(categoria)

        opcion = input("\nOpción: ")

    return recetas[int(opcion) - 1]


def leer_receta():
    """
    Permite al usuario seleccionar y leer una receta.
        1. Le indica al usuario que debe seleccionar una categoria.
        2. Le indica al usuario que debe seleccionar una receta de la categoria.
    """
    categoria_seleccionada = seleccionar_categoria()
    receta_seleccionada = seleccionar_receta(categoria_seleccionada)

    if receta_seleccionada:
        os.system("cls")
        receta = Path(ruta_raiz(), categoria_seleccionada, receta_seleccionada)
        print(f"{receta_seleccionada.split('.')[0]}:\n")
        print(receta.read_text())

    continuar()


def crear_receta():
    """
    Permite al usuario crear una nueva receta.
        1. Le indica al usuario que debe seleccionar una categoria.
        2. Le indica al usuario que debe escribir el nombre del archivo y el contenido de la receta.
        3. Crea el archivo en la carpeta de recetas.
        4. Muestra un mensaje de exito.
    """
    categoria_seleccionada = seleccionar_categoria()

    os.system("cls")
    nombre_del_archivo = input("Escribe el nombre de tu receta: ") + ".txt"
    contenido_del_archivo = input("Escribe la receta: ")

    ruta_archivo = Path(ruta_raiz(), categoria_seleccionada, nombre_del_archivo)
    archivo = open(ruta_archivo, "w")
    archivo.write(contenido_del_archivo)

    os.system("cls")
    print("La receta, ha sido creada exitosamente.")
    continuar()


def crear_categoria():
    """
    Permite al usuario crear una nueva categoria.
        1. Se pide al usuario que ingrese la nueva categoria.
        2. Se verifica que la categoria no exista.
        3. Se crea la categoria.
        4. Se muestra un mensaje de exito.
    """
    os.system("cls")
    categorias = todas_las_categorias()

    print("Categorias existentes: ")
    listar_todas_las_categorias()
    categoria_a_crear = input("\nIngresa la nueva categoria: ")

    while categoria_a_crear.lower() in [categoria.lower() for categoria in categorias]:
        categoria_a_crear = input("La categoria ya existe. Ingresa otra: ")

    os.mkdir(Path(ruta_raiz()) / categoria_a_crear)

    os.system("cls")
    print(f"La categoria '{categoria_a_crear}', ha sido creada exitosamente.")
    continuar()


def eliminar_receta():
    """
    Permite al usuario eliminar una receta.
        1. Se pide al usuario que seleccione la categoria.
        2. Se pide al usuario que seleccione la receta.
        3. Se elimina la receta.
        4. Se muestra un mensaje de exito.
    """
    categoria_seleccionada = seleccionar_categoria()
    receta_seleccionada = seleccionar_receta(categoria_seleccionada)

    Path(ruta_raiz(), categoria_seleccionada, receta_seleccionada).unlink()

    os.system("cls")
    print(f"La receta '{receta_seleccionada.split('.')[0]}', ha sido eliminada.")
    continuar()


def eliminar_categoria():
    """
    Permite al usuario eliminar una categoria.
        1. Se pide al usuario que seleccione la categoria.
        2. Se elimina la categoria.
        3. Se muestra un mensaje de exito.
    """

    categoria_seleccionada = seleccionar_categoria()
    eliminar_todas_las_recetas_por_categoria(categoria_seleccionada)
    Path(ruta_raiz(), categoria_seleccionada).rmdir()

    os.system("cls")
    print(f"La categoria '{categoria_seleccionada}', ha sido eliminada.")
    continuar()


def menu_principal():
    """
    Muestra el menú de selección principal
        1. Leer receta
        2. Crear receta
        3. Crear categoria
        4. ELiminar recetas
        5. Eliminar categoria
        6. Salir
    """

    finalizar_programa = False
    opcion = "x"

    while not finalizar_programa:
        bienvenida()
        listar_menu_principal()
        opcion = input("Opción: ")

        match opcion:
            case "1":
                leer_receta()
            case "2":
                crear_receta()
            case "3":
                crear_categoria()
            case "4":
                eliminar_receta()
            case "5":
                eliminar_categoria()
            case "6":
                finalizar_programa = True

    os.system("cls")


menu_principal()
