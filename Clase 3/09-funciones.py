# #funciones de imprimir 

# def imprimir(nombre):
#     print(nombre)



# imprimir("David")


# diccionario = {
#     "A":1,
#     "B":2,
#     "C":3
# }

# def imprimirdic (diccionario):
#     print(diccionario)

# imprimirdic(diccionario)


def calcular_sueldo(empleado):
    nombre = empleado["nombre"]
    tipo = empleado["tipo"]
    if tipo == "D":
        sueldo = 2000000
    elif tipo == "A":
        sueldo = 1000000
    else:
        sueldo = "SIN SALARIO"
    
    diccionarioSueldoEmpleado = {
        "nombre": nombre,
        "sueldo": sueldo,
        "tipo":tipo
    }

    return diccionarioSueldoEmpleado

empleado = {
    "id_empleado":123,
    "nombre":"David Pinchao",
    "tipo":"Z"
}


# calcular_sueldo(empleado)
print(calcular_sueldo(empleado))
