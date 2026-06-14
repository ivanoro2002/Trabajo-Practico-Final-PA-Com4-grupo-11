Desarrollar: Sist. Gestiíon de Biblioteca Digital. Funciones: Administrar libros, usuarios y prestamos.

Requerimentos - 
Gestión Libros (Titulo, Autor, ISBN, Año Publicado, Cantidad de pags, etc)
- Operaciones (Alta, Modificación, Baja, Listado)

Gestión Usuarios (Nombre, Apellido, DNI, CORREO, etc)
- Operaciones (Alta, Modificación, Baja, Listado)

Gestión Prestamos (Registar prestamos, devoluciones, consultar prestamos activos).
- Un libro no podrá prestarse si ya poseé un préstamo activo.
- Se deberá registrar fecha de préstamo y devolución.

Tecnicos: 
- Al menos una jerarquia de herencia. HECHO
- Al menos un comportamiento polimorfico. HECHO
- Al menos una relación de agrupación.  HECHO
- Al menos una relación de composición. HECHO
- Al menos un decorador propio e integrarlo dentro del sistema. PENDIENTE
- Al menos una metaclase (type) o una derivada de type. PENDIENTE
- Al menos un patrón de diseño, debidamente justificado. PENDIENTE

ADICIONAL
- Cant de stock (ejemplares) de libros, 1 o más. Si es más de un ejemplar necesita ID obligatoriamente un identificador (ID) porque el ISBN es el mismo para todos los ejemplares y no nos sirve para esta funcionalidad. HECHO
- UML incluido en el repositorio.
- README.md confeccionado correctamente.
- SINGLETON para separar bibliotecas (Si se crea más de una, para identificarla correctamente) -> Diseños de patron.
- Admin de datos (agg libros) -> JSON o libreria para cargar libros inicialmente.