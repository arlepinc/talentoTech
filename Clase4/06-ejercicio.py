class Persona:
    # nombre = ""
 

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):

    def __init__(self, nombre, apellido, num_cuenta, balance):
        super().__init__(nombre, apellido)
        self.num_cuenta = num_cuenta
        self.balance = balance
    
    def imprimir_cliente(self):
        print(f' \n Nombre: {self.nombre}\n Apellido: {self.apellido} \n Numero de cuenta: {self.num_cuenta} \n Balance: $ {self.balance}')


cliente1 = Cliente('David','Pinchao','12345',250000)
cliente1.imprimir_cliente()