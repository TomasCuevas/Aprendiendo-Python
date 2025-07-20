"""
    # MATCH: 
        En Python 3.10, se incorpora la coincidencia de patronese structurales mediante las declaraciones match y case. 
        Esto permite asociar acciones específicas basadas en las formas o patrones de tipos de datos complejos.
"""

serie = 'N-02'

match serie:
  case 'N-01':
    print("Samsung")
  case 'N-02':
    print("Nokia")
  case 'N-03':
    print("Motorola")
  case 'N-04':
    print("Google")
  case _:
    print("No se reconoce la serie")

cliente = {"nombre": "Juan", "edad": 25, "ciudad": "Buenos Aires"}
pelicula = {"titulo": "El secreto de la noche", "ficha_tecnica": {"genero": "horror", "duracion": 120, "director": "Jorge C. Antonio"}}
elementos = [cliente, pelicula, 'libro']

print("\n")
for e in elementos:
  match e:
    case {"nombre": nombre, "edad": edad, "ciudad": ciudad}:
      print(f"Es un cliente. Su nombres es '{nombre}'")
    case {"titulo": titulo, "ficha_tecnica": {"genero": genero, "duracion": duracion, "director": director}}:
      print(f"Es una pelicula. Su título es '{titulo}'")
    case _:
      print(f"Es un elemento no reconocido")