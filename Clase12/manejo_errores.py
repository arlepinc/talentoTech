def suma():

    try:
        num1 = int(input("Ingrese el primer numero:  "))
        num2 = int(input("Ingrese el segundo numero: "))
    
    except ValueError:
        print("ERROR: Solo se permite numeros, estas ingresando letras")

    else:
        suma = num1 + num2
        print(f'El resultado de la suma es {suma}')

    finally:

        print("ESTO SIEMPRE SE VA A EJECUTAR AUNQUE EXISTAN ERRORES")


# suma()


def dividir():

    try:
        num1 = int(input("Ingrese el numerador:  "))
        num2 = int(input("Ingrese el denominador: "))
        division = num1/num2
    
    except ValueError:
        print("ERROR: Solo se permite numeros, estas ingresando letras")

    else:
     
        print(f'El resultado de la division es {division}')

    finally:

        print("ESTO SIEMPRE SE VA A EJECUTAR AUNQUE EXISTAN ERRORES")

dividir()

    


