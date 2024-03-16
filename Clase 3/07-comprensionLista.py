palabra = "python"
numeros = [1,2,3,4,5]

#generar listas con for
lista = []
for letra in palabra:
    lista.append(letra)
print(lista)


#generar lista con comprension de listas
lista = [i for  i in palabra ]
print(lista)

lista2 =[i for i in numeros]
print(lista2)