import mysql.connector

conexion = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "admin",
    database = "tienda2"   
)

cursor = conexion.cursor()

# cursor.execute(""" 
# CREATE TABLE productos(
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     nombre VARCHAR(255) NOT NULL,
#     precio DECIMAL(10, 2) NOT NULL 
# )               
               
# """)


# cursor.execute("""
#  CREATE TABLE ventas (
#      id INT AUTO_INCREMENT PRIMARY KEY,
#      id_producto INT,
#      cantidad INT NOT NULL,
#      fecha DATE NOT NULL, 
#      FOREIGN KEY (id_producto) REFERENCES productos(id)  
#  )                            
# """)

# cursor.execute("""
#   INSERT INTO productos(nombre, precio) VALUES            
#   ('pan', 5000),
#   ('leche', 6000),
#   ('carne', 10000)             
# """)
# conexion.commit()

cursor.execute("""
  INSERT INTO ventas(id_producto, cantidad, fecha) VALUES            
  (1, 50, '2024-05-11'),
  (2, 60, '2024-05-11'),
  (3, 10, '2024-05-11')             
""")
conexion.commit()


