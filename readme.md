Integrantes: Alexis Politi, Aldana Ibarra, Ivan Valicenti Orosco



Este sistema de biblioteca permite administrar libros, usuarios y prestamos. Este lo dividimos en distintos gestores para mayor organización y que cada uno cumpla una función concreta.

Gestión Libros: Permite alta, baja, modificación y listado de libros, concluyendo con la consulta de stock de ejemplares mediante ISBN. En relación a esto, hemos contemplado la existencia de más de un ejemplar de un libro, por lo tanto, incluimos UUID para aleatorizar una ID única a cada libro. 

Gestión Usuarios: Realiza la alta, baja, modificación y listado de usuarios en el sistema. 

Gestión Prestamos: Registra prestamos, devuelve libros y consulta prestamos activos, si un ejemplar ya tiene un prestámo, no puede volver a pedirse, además, registra de manera automatica la fecha de prestamo y devolución. 

En cuanto al decorador, lo implementamos dentro de reg_info, está registrará el exito de cada operación en el sistema sin repetir código. 

Hemos optado por el patrón de diseño "SINGLETON" mediante una metaclase. Este garantiza la existencia de instancias únicas de cada gestor, evitando que se creen muchos objetos que administren listas diferentes a las originales (usuarios, libros, prestamos). 

Los conceptos de POO se ven reflejados en:

Herencia: Clase USER hereda de PERSON, reutilizando sus atributos. 
Polimorfismo: Mediante el metodo _str_() en distintas clases para mostrar su información de manera personalizada.
Composición: la clase Biblioteca contiene los libros, usuarios y préstamos, siendo la que organiza toda la información del sistema.


#diagrama de clases del codigo
![alt text](<diagrama de clases tp final PA.jpg>)