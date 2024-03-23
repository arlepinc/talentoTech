class Pajaro:
    alas = True

#definir atributos para una instancia de tipo objeto, creando un metodo constructor asi:  
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

#instanciamiento de la clase pajaro para crear el obj piolin
piolin = Pajaro('Azul','Terrestre')

#acceso a los atributos de clase y de instancia de "Pajaro"
print(piolin.color)
print(piolin.especie)
print(f'Mi parajaro es de color {piolin.color} y es de especie {piolin.especie}')


#-----------------------------------------------------------------------------------------------#

class Casa:

    def __init__(self, color, cantidad_pisos):
        self.color = color
        self.cantidad_pisos = cantidad_pisos

casa_blanca = Casa("blanco", 4)
print(f'La casa es de color {casa_blanca.color} y tiene {casa_blanca.cantidad_pisos} pisos')

#-------------------------------------------------------------------------------------------------#

class Cubo:
    caras = 6

    def __init__(self, color):
        self.color = color

cubo_rojo = Cubo("rojo")
print(f'el cubo tiene {cubo_rojo.caras} caras y es de color {cubo_rojo.color}')


#------------------------------------------------------------------------------------------------#
class Personaje:
    real = False

    def __init__(self, especie, magico, edad):
        self.especie = especie
        self.magico = magico
        self.edad = edad

harry_potter = Personaje('Humano',True,17)

print(f'Harry Potter es un personaje {harry_potter.real} de especie {harry_potter.especie}, ¿es magico? {harry_potter.magico} y su edad es de {harry_potter.edad} años')


