import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "admin",
    database = "testdb5"    
)

my_cursor = mydb.cursor()

my_sql = "DROP TABLE IF EXISTS users"