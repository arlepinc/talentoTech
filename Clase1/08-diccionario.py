diccionario = {
    "nombre":"David",
    "apellido":"Lopez",
    "edad":23,
    "profesion":"docente"
}

print(diccionario)
print(diccionario["nombre"])
print(diccionario["profesion"])

diccionario2 ={
    "azul":"blue",
    "amarillo":"yellow",
    "rojo":"red"
}

#agregar un nuevo elemento haciendo uso de clave:valor
diccionario2["verde"] = "green"
print(diccionario2)

#modificando el valor de una cable 
diccionario2["amarillo"] = "amarillo"
print(diccionario2)


diccionario3 = {
    "nombre":"arley",
    "apellido":"pinchao",
    "profesion":"docente",
    "asiganturas":["ingles" ,"sociales","español", "matematicas"]

}

print(diccionario3["asiganturas"][3])
