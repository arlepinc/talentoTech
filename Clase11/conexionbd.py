import mysql.connector

def conexionbd():

    conexion = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "0000",
        database = "gestion_estudiantes"

    )
    print ("conexion exitosa")
    return conexion
    