import uuid                        # MODULO PARA ALEATORIZAR UNA ID DE CADA LIBRO AGG (ALDANA)

class Biblioteca: 
    def __init__(self):
        self.users = []
        self.libros = []
        self.prestamos = []         

class Libro:
    def __init__(self, titulo, autor, isbn, año_publicado, cant_pags):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn 
        self.año_publicado = año_publicado                                     # A. DEBE SUBIR LIBROS CORRECTAMENTE (ACÁ)
        self.cant_pags = cant_pags
        self.id = str(uuid.uuid4()) 
        self.stock = 0               

    def __str__(self):                              
        return f"{self.titulo} - {self.autor} - {self.isbn} - {self.año_publicado} - {self.cant_pags}"

class Person:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):                              
        return f"{self.nombre} - {self.apellido}"
    
class User(Person):     
    def __init__(self, nombre, apellido, dni, correo):
        super().__init__(nombre, apellido)
        self.dni = dni
        self.correo = correo
    
    def __str__(self):                              
        return f"{self.nombre} - {self.apellido} - {self.dni} - {self.correo}"

class Gestion_Libros():
    def __init__(self):
        self.libros = []
        self.disponible = True
        self.stock = 0

    def agg_libro(self, libro):                   # DAR ALTA      
        if libro == self.libros:
            return "Este libro ya existe."
        else: 
            self.libros.append(libro)                        
            self.stock += 1                        

    def del_libro(self, id):            
        for i in self.libros:
            if i.id == id:
                self.libros.remove(i)
                self.stock -= 1
            else:
                return "El libro no existe."

    def modify_libro(self, isbn, new_titulo, new_cant_pags):    #ISBN = IDENTIFICADOR DE LIBROS
        for l in self.libros:
            if l.isbn == isbn:   
                l.titulo = new_titulo                       
                l.cant_pags = new_cant_pags
        return "Libro no encontrado."
                
class Gestion_Usuario:
    def __init__(self):
        self.users = []

    def agg_user(self, usuario):
        if usuario == self.users:
            return "El usuario ya existe."
        self.users.append(usuario)

    def del_user(self, dni):
        for u in self.users:
            if u.dni == dni:
                self.users.remove(u)                
        return "El usuario no existe."    

    def modify_user(self, dni, new_correo):
        for u in self.users:                      
            if u.dni == dni:                          
                self.correo = new_correo
        return "El usuario no existe en la base de datos."

biblioteca = Biblioteca()         # A. 
gestor_l = Gestion_Libros()         # A.
gestor_p = Gestion_Usuario()
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 25, 1950, 66)          
print(libro1)
gestor_l.agg_libro(libro1)          # A.
persona1 = User("Leonel", "Politi", 45489751654, "alexis@gmail.com")
print(persona1)