import mysql.connector

mydb = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "0000",
    database = "bdtest"
)

my_cursor = mydb.cursor()

#Sentencia SQL para mostrar los datos de una tabla 
my_cursor.execute("SELECT * FROM users")

#para mostrar la informacion usamos la funcion fetchall que nos trae todos los registros;
resultado = my_cursor.fetchall()

print(resultado)

for row in resultado:
    print(row)