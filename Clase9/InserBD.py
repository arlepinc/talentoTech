import mysql.connector

mydb = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "0000",
    database = "bdtest"
)

my_cursor = mydb.cursor()

#INSERTADNO DATOS EN LA TABLA USERS, CON VARIABLES Y EL CURSOR 

#Asigno la primera parte de la sentencia SQL con los posicionamientos %s
sentenciaSQL = "INSERT INTO users(name, email, age) VALUES (%s, %s, %s)"

#Pasamos los datos a las posiciones (columnas de la tabla) se puede pasar un valor o varios con la lista para que haga las insercciones
datos = [("David","david@gmail.com",30),
         ("Sandra","sandra@gmail.com",29),
         ("Camila","camila@gmail.com",35)]

#my_cursor.execute(sentenciaSQL,datos) (inserta una sola fila con los datos entregados)
my_cursor.executemany(sentenciaSQL,datos) #inserta varias filas con la lista de dats entergada a la variable.
mydb.commit()  #el commit ayuda a que la inserccion sea exitosa y llegue hasta tabla