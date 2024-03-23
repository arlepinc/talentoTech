# class Pajaro:

#     alas = True

#     def __init__(self,color,especie):
#         self.color = color
#         self.especie = especie
    
#     def piar(self):
#         print(f'mi canto es "pio pio", soy de color {self.color}')

#     def volar(self, metros):
#         print(f'el pajaro vuela {metros} metros')

# piolin = Pajaro('amarillo','terrestre')
# piolin.piar()
# piolin.volar(15)


#---------------------EJERCICIOS DE METODOS---------------------------------------#

class Perro:

    def ladrar(self):
        print('GUAU GUAU')

goofy = Perro()
goofy.ladrar()

#-----------------------------------------------------------------------------#

class Mago:

    def lanzar_hechizo(self):
        print("ABRACADABRA")

berlin = Mago()
berlin.lanzar_hechizo()

#------------------------------------------------------------------#

class Alarma:

    def postergar_alarma(self,cantidad_minutos):
        print(f'la alarma ha sido pospuesta {cantidad_minutos} minutos')

despertador = Alarma()
despertador.postergar_alarma(10)

