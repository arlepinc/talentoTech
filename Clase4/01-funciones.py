#Argumentos


def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)

suma(10,50)
suma(1,3)
suma(2,4,6,8,10)


# entrgar datos de un diccionario para usarlos por su clave
def obtener_productos (**datos):
    print(datos["id"])
    # print(datos)

obtener_productos(id = "123", nombre = "celular" , descripcion = "samsung")