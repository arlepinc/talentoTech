import mysql.connector



mydb = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "0000",
    database = "bdtest"
)


my_cursor = mydb.cursor()

my_cursor.execute("CREATE TABLE users (name VARCHAR(50), email VARCHAR(100), age INT(10), user_id INT AUTO_INCREMENT PRIMARY KEY)")




