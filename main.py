class Biblioteca: 
    def __init__(self):
        self.users = []
        self.libros = []
        self.prestamos = []   
               
class Gestion_Usuario:
    def __init__(self):
        self.users = []

    def agg_user(self, usuario):
        for u in self.users:
            if u == usuario:
                return "El usuario ya existe."
            else:
                self.users.append(usuario)

    def del_user(self, usuario):
        for u in self.users:
            if u == usuario:
                self.users.remove(usuario)                
            else:
                return "El usuario no existe."    

    def modify_user(self, dni, new_correo):
        for self.dni in self.users:
            if self.dni == dni:                          
                self.correo = new_correo
            else:
                return "El usuario no existe en la base de datos."
            
    def __str__(self):
        return f"{self.nombre} - {self.apellido} - {self.dni} - {self.correo}" 
  
class Person:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class User(Person): 
    def __init__(self, nombre, apellido, dni, correo):
        super().__init__(nombre, apellido)
        self.dni = dni
        self.correo = correo

class Gestion_Libros:
    def __init__(self, titulo, autor, isbn, año_publicado, cant_pags):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn 
        self.año_publicado = año_publicado
        self.cant_pags = cant_pags
        self.disponible = True

    def __str__(self):                              
        f"{self.titulo} - {self.autor}"                 

    def agg_libro(self, libro):                   # DAR ALTA
        for l in self.libros:
            if l == libro:
                return "Este libro ya existe."
            else:
                self.libros.append(libro)                    
    
    def del_libro(self, isbn):            
        for i in self.libros:
            if i == isbn:
                self.libros.remove(i)
            else:
                return "El libro no existe."

    def modify_libro(self, isbn, new_titulo, new_cant_pags):    #ISBN = IDENTIFICADOR DE LIBROS (ID)
        for self.isbn in self.libros:
            if self.isbn == isbn:   
                self.titulo = new_titulo                       
                self.cant_pags = new_cant_pags
            else:
                return "Libro no encontrado."



