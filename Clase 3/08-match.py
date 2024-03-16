"""Antes para hacer varias opciones en python se hacia con un if"""

serie = "N-02"

if serie == "N-01":
    print("Samsung")
elif serie == "N-02":
    print("Nokia")
elif serie == "N-03":
    print("Motorola")
else:
    print("Serie no encontrada en las marcas")


"""Despues de la version de python 3.10 se incorporo **match** que sirve como un switch"""

serie2 = "N-03"

match serie2:
    case "N-01":
        print("Samsung")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("Motorola")
    case _:
        print("Serie no encontrada en las marcas")


    