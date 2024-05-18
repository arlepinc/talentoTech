import mysql.connector

mydb = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "0000",
    database = "bdtest"
)

my_cursor = mydb.cursor()

#Consulta usando where para establecer condiciones
my_cursor.execute("SELECT * FROM users WHERE age > 30")

resultado = my_cursor.fetchall()

for row in resultado:
    print(row)
    # print(row[0]) #accediendo a la posicion de la tupla del resultado
    print(f"el nombre es {row[0]} y la edad es {row[2]}")

   