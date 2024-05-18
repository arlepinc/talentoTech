import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "admin",
    database = "testdb5"    
)

my_cursor = mydb.cursor()
my_cursor.execute("SELECT * FROM users")

resultado = my_cursor.fetchall()

for row in resultado:
    print(row)