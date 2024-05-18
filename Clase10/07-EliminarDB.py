import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "admin",
    database = "testdb5"    
)

my_cursor = mydb.cursor()

my_sql = "DELETE FROM users WHERE user_id = 4"
my_cursor.execute(my_sql)
mydb.commit()