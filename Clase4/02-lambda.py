# lambda es igual a un for, la estructura recibe i y un elemento iterable (listas, tuplas, diccionario)

# funcion filter
lista = [3,10,5,7,18, 50]
resultado = list(filter(lambda num : num > 10, lista))
print(resultado)

# funcion map
lista2 = [2,7,9,13]
resultado2 = list(map(lambda num : num ** 2 , lista2))
print(resultado2)

palabaras = ['manzana','pera','papaya', 'limon']
prefijo = 'frutas'
union = list(map(lambda palabra : prefijo + ' ' + palabra, palabaras))
print(union)

for palabra in palabaras:
    print(prefijo + ' ' + palabra)






