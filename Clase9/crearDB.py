#CONEXION A BASES DE DATOS
#pip install mysql-connector-python: Este comando debe usarse en un cmd y sirve para conectar la BD con Python cpn el driver mysql.connector

import mysql.connector


mydb = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "0000"
)


print (mydb)

#Creamos un cursor, para poder ejecutar sentencias SQL
my_cursor = mydb.cursor()

my_cursor.execute("CREATE DATABASE bdtest")

