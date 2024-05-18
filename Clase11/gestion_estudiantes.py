from conexionbd import conexionbd #importamos el archivo donde esta la conexion a la base de datos de gestion_estudiantes

def crearTablaEstudiantes():
    conexion = conexionbd() #le pasamos la funcion de la conexion de la bd de g.estudiantes a una variable para reusarla
    my_cursor = conexion.cursor() # creamos el cursor para trabajar con MYSQL
    
    consulta = """
    CREATE TABLE estudiantes(
    id_estudiante INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    apellido VARCHAR(255),
    edad INT,
    calificacion FLOAT
    )
    """

    my_cursor.execute(consulta) #llamamos el cursor para ejecutar la consulta SQL y le pasamo la variable dond esta la consulatA
    print('Tabla estudiantes creada con exito')
    my_cursor.close()
    conexion.close()


def InsertarEstudiante(nombre, apellido, edad, calificacion):
    conexion = conexionbd()
    my_cursor = conexion.cursor() 

    consultaSQL = """
    INSERT INTO estudiantes(nombre, apellido, edad, calificacion)
    VALUES(%s, %s, %s, %s)
    """

    datos = (nombre, apellido, edad, calificacion)
    my_cursor.execute(consultaSQL, datos)
    conexion.commit()
    my_cursor.close()
    conexion.close()
    print("Estudiante insertado correctamente")


def mostrarCalificaciones():
    conexion = conexionbd()
    my_cursor = conexion.cursor() 

    consultaSQL = "SELECT nombre, apellido, calificacion FROM estudiantes"
    my_cursor.execute(consultaSQL)
    calificaciones = my_cursor.fetchall()

    for estudiante in calificaciones:
        print(f'Nombre: {estudiante[0]}, Apellido: {estudiante[1]}, Calificacion: {estudiante[2]}')

    
    my_cursor.close()
    conexion.close()

def actualizarCalificacion(id_estudiante, nueva_calificacion):
    conexion = conexionbd()
    my_cursor = conexion.cursor() 

    consultaSQL = """UPDATE estudiantes
                     SET calificacion = %s
                     WHERE id_estudiante = %s
                                            """
    
    datos = (nueva_calificacion, id_estudiante)

    my_cursor.execute(consultaSQL,datos)
    conexion.commit()

    my_cursor.close()
    conexion.close()
    print("Calificacion actualizada con exito")


def eliminarEstudiante (id_estudiante):
    
    conexion = conexionbd()
    my_cursor = conexion.cursor() 

    consultaSQL = """
    DELETE FROM estudiantes
    WHERE id_estudiante = %s
    """
    datos = (id_estudiante,)

    my_cursor.execute(consultaSQL,datos)
    conexion.commit()

    my_cursor.close()
    conexion.close()

    print("Estudiante eliminado con exito")


# crearTablaEstudiantes()
# InsertarEstudiante('Arley','Pinchao',28,4.5)
# InsertarEstudiante('Sandra','Ramirez',29,5)
#InsertarEstudiante('Danilo','Calpa',31,3.8)
# mostrarCalificaciones()
# actualizarCalificacion(3,1)
# eliminarEstudiante(5)






