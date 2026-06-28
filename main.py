import uuid
from datetime import date

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.users = []
        self.prestamos = []

class SingletonMeta(type):
    _instancias = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instancias:
            cls._instancias[cls] = super().__call__(*args, **kwargs)
        return cls._instancias[cls]

def reg_info(func):
    def func_retorno(*args, **kwargs):
        print("\nEjecutando operación...")
        resultado = func(*args, **kwargs)
        print(resultado)
        return resultado
    return func_retorno

class Libro:
    def __init__(self, titulo, autor, isbn, año_publicado, cant_pags):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.año_publicado = año_publicado
        self.cant_pags = cant_pags
        self.id = str(uuid.uuid4())      # Identificador único del ejemplar

    def __str__(self):
        return (f"Título: {self.titulo} | "
                f"Autor: {self.autor} | "
                f"ISBN: {self.isbn} | "
                f"ID: {self.id}")

class Person:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class User(Person):
    def __init__(self, nombre, apellido, dni, correo):
        super().__init__(nombre, apellido)
        self.dni = dni
        self.correo = correo
    def __str__(self):
        return (f"Nombre: {self.nombre} {self.apellido} | "
                f"DNI: {self.dni} | "
                f"Correo: {self.correo}")
    
# GESTIÓN LIBROS

class Gestion_Libros(metaclass=SingletonMeta):
    def __init__(self, biblioteca):
        self.biblioteca = biblioteca

    @reg_info
    def agg_libro(self, libro):
        self.biblioteca.libros.append(libro)
        return f"Se agregó un ejemplar de {libro.titulo}"

    @reg_info
    def del_libro(self, id_libro):
        for libro in self.biblioteca.libros:
            if libro.id == id_libro:
                self.biblioteca.libros.remove(libro)
                return f"El ejemplar '{libro.titulo}' fue eliminado."
        return "Ejemplar no encontrado."

    @reg_info
    def modify_libro(self, id_libro, nuevo_titulo, nuevas_paginas):
        for libro in self.biblioteca.libros:
            if libro.id == id_libro:
                libro.titulo = nuevo_titulo
                libro.cant_pags = nuevas_paginas
                return "Libro modificado correctamente."
        return "Libro no encontrado."

    @reg_info
    def listar_libros(self):
        if not self.biblioteca.libros:
            return "No hay libros registrados."
        print("\n===== LISTA DE LIBROS =====")
        for libro in self.biblioteca.libros:
            print(libro)
        return "Listado completado."

    @reg_info
    def consultar_stock(self, isbn):
        cantidad = sum(1 for libro in self.biblioteca.libros if libro.isbn == isbn)
        return f"Stock disponible para ISBN {isbn}: {cantidad}"

 # GESTIÓN USUARIOS

class Gestion_Usuario(metaclass=SingletonMeta):
    def __init__(self, biblioteca):
        self.biblioteca = biblioteca

    @reg_info
    def agg_user(self, usuario):
        if any(u.dni == usuario.dni for u in self.biblioteca.users):
            return "El usuario ya existe."
        self.biblioteca.users.append(usuario)
        return f"El usuario '{usuario.nombre}' fue agregado correctamente."

    @reg_info
    def del_user(self, dni):
        for usuario in self.biblioteca.users:
            if usuario.dni == dni:
                self.biblioteca.users.remove(usuario)
                return f"El usuario {usuario.nombre} fue eliminado."
        return "Usuario no encontrado."

    @reg_info
    def modify_user(self, dni, nuevo_correo):
        for usuario in self.biblioteca.users:
            if usuario.dni == dni:
                usuario.correo = nuevo_correo
                return "Usuario modificado correctamente."
        return "Usuario no encontrado."

    @reg_info
    def listar_users(self):
        if not self.biblioteca.users:
            return "No hay usuarios registrados."
        print("\n===== LISTA DE USUARIOS =====")
        for usuario in self.biblioteca.users:
            print(usuario)
        return "Listado completado."
    
class Prestamo:

    def __init__(self, libro, usuario):
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = date.today()
        self.fecha_devolucion = None

    @property
    def activo(self):
        return self.fecha_devolucion is None

    def devolver(self):
        self.fecha_devolucion = date.today()

    def __str__(self):
        estado = "Activo" if self.activo else "Devuelto"

        return (f"Libro: {self.libro.titulo} | "
                f"Usuario: {self.usuario.nombre} {self.usuario.apellido} | "
                f"Préstamo: {self.fecha_prestamo} | "
                f"Devolución: {self.fecha_devolucion} | "
                f"Estado: {estado}")
    
class Gestion_Prestamos(metaclass=SingletonMeta):

    def __init__(self, biblioteca):
        self.biblioteca = biblioteca

    def libro_prestado(self, id_libro):
        return any(
            prestamo.libro.id == id_libro and prestamo.activo
            for prestamo in self.biblioteca.prestamos
        )

    @reg_info
    def registrar_prestamo(self, isbn, dni): # EJEMPLAR E IDENTIFICACIÓN DE USUARIO 
        usuario = None
        for u in self.biblioteca.users:
            if u.dni == dni:
                usuario = u
                break
        if usuario is None:
            return "Usuario no encontrado."
        libro = None
        for l in self.biblioteca.libros:
            if l.isbn == isbn and not self.libro_prestado(l.id):
                libro = l
                break
        if libro is None:
            return "No hay ejemplares disponibles."
        prestamo = Prestamo(libro, usuario)
        self.biblioteca.prestamos.append(prestamo)
        return "Préstamo registrado correctamente."

    @reg_info
    def devolver_libro(self, isbn, dni):
        for prestamo in self.biblioteca.prestamos:
            if (prestamo.libro.isbn == isbn
                    and prestamo.usuario.dni == dni
                    and prestamo.activo):
                prestamo.devolver()
                return "Libro devuelto correctamente."
        return "No existe un préstamo activo para ese usuario."

    @reg_info
    def listar_prestamos_activos(self):
        activos = [p for p in self.biblioteca.prestamos if p.activo]
        if not activos:
            return "No hay préstamos activos."
        print("\n===== PRÉSTAMOS ACTIVOS =====")
        for prestamo in activos:
            print(prestamo)
        return "Listado completado."


biblioteca = Biblioteca()

gestion_libros = Gestion_Libros(biblioteca)
gestion_usuarios = Gestion_Usuario(biblioteca)
gestion_prestamos = Gestion_Prestamos(biblioteca)

libro1 = Libro("Harry Potter", "J. K. Rowling", "9788478884452", 1997, 320)
libro2 = Libro("Harry Potter", "J. K. Rowling", "9788478884452", 1997, 320)

gestion_libros.agg_libro(libro1)
gestion_libros.agg_libro(libro2)

usuario1 = User("Alexis", "González", 45111222, "alexis@gmail.com")
gestion_usuarios.agg_user(usuario1)

gestion_usuarios.listar_users()

gestion_prestamos.registrar_prestamo("9788478884452", 45111222)

gestion_prestamos.listar_prestamos_activos()

gestion_prestamos.devolver_libro("9788478884452", 45111222)
