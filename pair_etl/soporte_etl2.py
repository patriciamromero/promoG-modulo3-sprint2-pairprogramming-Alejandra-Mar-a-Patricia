#%% comentarios para librerías
# Importar librería para la conexión con MySQL
# Esta librería permite conectar a bases de datos MySQL desde Python
import mysql.connector

#%%
def creacion_bbdd_tablas(query, contraseña, nombre_bbdd=None,host="localhost",user="root"):
    """
    Esta función crea una base de datos y tablas si no existen.
    """

    if nombre_bbdd is not None:  # Comprobar si se proporciona un nombre de base de datos
        cnx = mysql.connector.connect(
            user=user,
            password=contraseña,
            host=host
        )

        mycursor = cnx.cursor()

        try:
            mycursor.execute(query)
            print(mycursor)  # Imprimir el cursor del resultado (opcional)

        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)
    else:
        cnx = mysql.connector.connect(
            user="root",
            password=contraseña,
            host=host,
            database=nombre_bbdd  # Usar la base de datos proporcionada
        )

        mycursor = cnx.cursor()

        try:
            mycursor.execute(query)
            print(mycursor)  # Imprimir el cursor del resultado (opcional)
            cnx.close()  # Cerrar la conexión

        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)
        cnx.close()  # Cerrar la conexión si hay un error

def insertar_datos(query, contraseña, nombre_bbdd, lista_tuplas,host="localhost",user="root"):
    """
    Esta función inserta datos en una tabla de una base de datos MySQL.

    """

    cnx = mysql.connector.connect(
        user=user,
        password=contraseña,
        host=host,
        database=nombre_bbdd
    )

    mycursor = cnx.cursor()

    try:
        mycursor.executemany(query, lista_tuplas)  # Insertar múltiples filas con executemany
        cnx.commit()  # Confirmar la inserción
        print(mycursor.rowcount, "registro/s insertado/s.")
        cnx.close()  # Cerrar la conexión

    except mysql.connector.Error as err:
        print(err)
        print("Error Code:", err.errno)
        print("SQLSTATE", err.sqlstate)
        print("Message", err.msg)
        cnx.close()  # Cerrar la conexión si hay un error

# Definición de consultas SQL para crear base de datos y tablas
query_creacion_bbdd = "CREATE SCHEMA IF NOT EXISTS `Empresa_f`;"

query_tabla_producto = """CREATE TABLE IF NOT EXISTS `Empresa_f`.`productos` (
  `Id_producto` VARCHAR(45) NOT NULL,
  `Nombre_producto` VARCHAR(100) NOT NULL,
  `Categoría` VARCHAR(100) NOT NULL,
  `Precio` FLOAT NOT NULL,
  `Origen` VARCHAR(45) NOT NULL,
  `Descripcion` VARCHAR(200) NOT NULL,
  PRIMARY KEY (`Id_producto`));"""

query_tabla_clientes = """CREATE TABLE IF NOT EXISTS `Empresa_f`.`clientes` (
  `Id_cliente` INT NOT NULL,
  `First_name` VARCHAR(100) NULL,
  `Last_name` VARCHAR(100) NULL,
  `Email` VARCHAR(100) NOT NULL,
  `Gender` VARCHAR(45) NOT NULL,
  `City` VARCHAR(100) NOT NULL,
  `Country` VARCHAR(45) NOT NULL,
  `Address` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`Id_cliente`));"""

# Definición de consultas SQL para insertar datos
query_insertar_producto = "INSERT INTO productos (Id_producto, Nombre_producto, Categoría, Precio, Origen, Descripcion) VALUES (%s, %s, %s, %s, %s, %s)"

query_insertar_clientes = "INSERT INTO clientes (Id_cliente, First_name, Last_name, Email, Gender, City, Country, Address) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

