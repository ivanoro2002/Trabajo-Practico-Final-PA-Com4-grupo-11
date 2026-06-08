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





