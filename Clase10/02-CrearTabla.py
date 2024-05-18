import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "admin",
    database = "testdb5"    
)

my_cursor = mydb.cursor()

my_cursor.execute("CREATE TABLE users (name VARCHAR(50), email VARCHAR(100), age INTEGER(10), user_id INTEGER AUTO_INCREMENT PRIMARY)")

