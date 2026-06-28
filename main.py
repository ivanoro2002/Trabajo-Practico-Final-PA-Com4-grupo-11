import uuid
from datetime import date

class Biblioteca:
    def _init_(self):
        self.libros = []
        self.users = []
        self.prestamos = []

class SingletonMeta(type):
    _instancias = {}
    def _call_(cls, *args, **kwargs):
        if cls not in cls._instancias:
            cls.instancias[cls] = super().call_(*args, **kwargs)
        return cls._instancias[cls]

def reg_info(func):
    def func_retorno(*args, **kwargs):
        print("\nEjecutando operación...")
        resultado = func(*args, **kwargs)
        print(resultado)
        return resultado
    return func_retorno

class Libro:
    def _init_(self, titulo, autor, isbn, año_publicado, cant_pags):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.año_publicado = año_publicado
        self.cant_pags = cant_pags
        self.id = str(uuid.uuid4())      # Identificador único del ejemplar

    def _str_(self):
        return (f"Título: {self.titulo} | "
                f"Autor: {self.autor} | "
                f"ISBN: {self.isbn} | "
                f"ID: {self.id}")


class Person:
    def _init_(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    def _str_(self):
        return f"{self.nombre} {self.apellido}"

class User(Person):
    def _init_(self, nombre, apellido, dni, correo):
        super()._init_(nombre, apellido)
        self.dni = dni
        self.correo = correo
    def _str_(self):
        return (f"Nombre: {self.nombre} {self.apellido} | "
                f"DNI: {self.dni} | "
                f"Correo: {self.correo}")
    
# GESTIÓN LIBROS

class Gestion_Libros(metaclass=SingletonMeta):
    def _init_(self, biblioteca):
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
    def _init_(self, biblioteca):
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