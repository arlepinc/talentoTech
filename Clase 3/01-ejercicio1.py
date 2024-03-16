"""

La consigna es la siguiente: vas a crear un programa que primero le pida al usuario que
ingrese un texto. Puede ser un texto cualquiera: un artículo entero, un párrafo, una frase, un
poema, lo que quiera. Luego, el programa le va a pedir al usuario que también ingrese tres
letras a su elección y a partir de ese momento nuestro código va a procesar esa información
para hacer cinco tipos de análisis y devolverle al usuario la siguiente información:

1. Primero: ¿cuántas veces aparece cada una de las letras que eligió? Para lograr esto, te
recomiendo almacenar esas letras en una lista y luego usar algún método propio de string
que nos permita contar cuantas veces aparece un sub string dentro del string. Algo que
debes tener en cuenta es que al buscar las letras pueden haber mayúsculas y minúsculas
y esto va a afectar el resultado. Lo que deberías hacer para asegurarte de que se
encuentren absolutamente todas las letras es pasar, tanto el texto original como las
letras a buscar, a minúsculas.


"""

# parrafo = input("ingrese un parrafo de su poema favorito")
# print(parrafo)

# listaLetras = []

# listaLetras.append(input("ingrese una letra"))
# listaLetras.append(input("ingrese una letra"))
# listaLetras.append(input("ingrese una letra"))
# print(listaLetras)


# parrafo = parrafo.lower()


# for i in range(len(listaLetras)):
#     listaLetras[i] = listaLetras[i].lower()


# # print(listaLetras)
# # print(parrafo)


# print(parrafo.count(listaLetras[0]))
# print(parrafo.count(listaLetras[1]))
# print(parrafo.count(listaLetras[2]))


"""
2.
Segundo: le vas a decir al usuario cuántas palabras hay a lo largo de todo el texto. Y para lograr esta parte, 
recuerda que hay un método de string que permite transformarlo en una lista y que luego hay una función que
permite averiguar el largo de una lista.

 
"""

# parrafo = input("ingrese un parrafo de su poema favorito")
# # parrafo = parrafo.split()
# print(parrafo)
# print(len(parrafo))

"""
Tercero: nos va a informar cuál es la primera letra del texto y cuál es la última. 
Aquí claramente echaremos mano de la indexación.


"""

# print(parrafo[0])
# print(parrafo[-1])


"""
Cuarto: el sistema nos va a mostrar cómo quedaría el texto si invirtiéramos el orden de las palabras. 
¿Acaso hay algún método que permita invertir el orden de una lista, 
y otro que permita unir esos elementos con espacios intermedios? Piénsalo.


"""

parrafo = input("ingrese un parrafo de su poema favorito")
parrafo = parrafo.split()
parrafo.reverse()
parrafo2 = parrafo
final = " ".join(parrafo2)
print(final)


"""
Y por último: el sistema nos va a decir si la palabra “Python” se encuentra dentro del texto. 
Esta parte puede ser algo complicada de imaginársela, pero te voy a dar una pista: puedes usar booleanos para hacer tu averiguación
 y un diccionario para encontrar la manera de expresarle al usuario tu respuesta.
"""

parrafo = input("ingrese un parrafo de su poema favorito")
parrafo.lower()
buscar = "python" in parrafo

diccionario = {}
diccionario ["python"] = buscar
print(diccionario)



