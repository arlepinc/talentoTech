import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "0000",
    database = "universidad"    
)

my_cursor = mydb.cursor()

# my_cursor.execute("""CREATE TABLE estudiantes (

# id_estudiante INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
# nombre VARCHAR(25),
# edad INT(3));""")


# my_cursor.execute("""CREATE TABLE cursos (

# id_curso INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
# nombre_curso VARCHAR(50),
# creditos INT (2));""")


# my_cursor.execute("""
#   INSERT INTO estudiantes(nombre,edad) VALUES            
#   ('David', 28),
#   ('Sandra',29),
#   ('Danilo', 31)            
# """)
# mydb.commit()


# my_cursor.execute(""" INSERT INTO cursos(nombre_curso, creditos) VALUES
#                   ('Ingles',3),
#                   ('Programacion', 3),
#                   ('Catedra Unadista',2)""")
# mydb.commit()


# my_cursor.execute("SELECT * FROM estudiantes")
# resultado = my_cursor.fetchall()

# for row in resultado:
#     print(row)



# my_cursor.execute("SELECT * FROM cursos")
# resultado2 = my_cursor.fetchall()

# for columna in resultado2:
#     print(columna)




