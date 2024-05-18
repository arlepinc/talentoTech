import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "admin",
    database = "testdb5"    
)

my_cursor = mydb.cursor()

sentenciaSql = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)" 
datos = [("Johana", "johana@gmail.com", 20),
         ("Jorge", "jorge@gmail.com",30),
         ("Camila", "camilita@hotmail.com", 35)]

my_cursor.executemany(sentenciaSql, datos)
mydb.commit()




