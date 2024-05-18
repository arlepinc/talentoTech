import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "admin",
    database = "testdb5"    
)

my_cursor = mydb.cursor()


my_sql = "UPDATE users SET email = 'johan@hotmail.com' WHERE user_id = 1"
my_cursor.execute(my_sql)
mydb.commit()