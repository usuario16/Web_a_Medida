import sqlite3

# - Este es un archivo aparte que se utilizó con el fin de crear 
# la tabla de consultas que utiliza el sitio web.

# - La utilización de este fichero ha sido utilidad una sola vez, 
# y esta será la única, ya que NO se pueden crear dos tablas con 
# el mismo nombre dentro de una misma base de datos.


# Definición de la función para crear la tabla
def crear_tabla():
    cursor = sqlite3.connect('consultas.db')
    try:
        cursor.execute(
            """
            CREATE TABLE consultas (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                correo TEXT(50) NOT NULL,
                consulta TEXT(500) NOT NULL
            );
            """
        )
        print('Tabla creada con exito...!')
    except:
        print('La tabla ya ha sido creada...')

# Llamada para crear
crear_tabla()
