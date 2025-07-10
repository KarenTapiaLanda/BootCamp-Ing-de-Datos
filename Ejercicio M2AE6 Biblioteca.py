class Libro:
    def __init__(self, titulo, autor, stock):
        self.titulo = titulo
        self.autor = autor
        self.stock = stock
class LibroNoDisponibleError(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)
class Biblioteca:
    def __init__(self):
        self.catalogo = {}  # Diccionario con libros, clave = título

    def agregar_libro(self, libro):
        self.catalogo[libro.titulo] = libro

    def prestar_libro(self, titulo):
        if titulo in self.catalogo:
            libro = self.catalogo[titulo]
            if libro.stock > 0:
                libro.stock -= 1
                print(f" Libro prestado: {titulo}. Stock restante: {libro.stock}")
            else:
                raise LibroNoDisponibleError(f" No hay stock disponible para: '{titulo}'.")
        else:
            raise LibroNoDisponibleError(f" El libro '{titulo}' no está en el catálogo.")
# Crear biblioteca y agregar libros
biblioteca = Biblioteca()
biblioteca.agregar_libro(Libro("1984", "George Orwell", 2))
biblioteca.agregar_libro(Libro("Cien años de soledad", "Gabriel García Márquez", 1))

# Probar préstamo de libros
try:
    biblioteca.prestar_libro("1984")  #  debería funcionar
    biblioteca.prestar_libro("1984")  #  último ejemplar
    biblioteca.prestar_libro("1984")  #  sin stock
except LibroNoDisponibleError as e:
    print(e)

try:
    biblioteca.prestar_libro("El Principito")  #  no existe
except LibroNoDisponibleError as e:
    print(e)
