conjunto = {1,2,3,"cadena"}

conjunto2 = set


print(type(conjunto))
print(conjunto)


#metodos

#agregar elementos a un conjunto
conjunto.add("david")
conjunto.add("24")
print(conjunto)

#eliminar elemento de un conjunto
conjunto.discard("david")
print(conjunto)

#buscar un elemento en conjunto
print(1 in conjunto)
print(1 not in conjunto)

#limpiar conjunto
conjunto.clear()
print(conjunto)