letras = ["a","b","c","d"]
numeros = [1,2,3,4,5]
combinacion = list(zip(letras,numeros))
print(combinacion)

for letras, numeros in combinacion:
    print(f"{letras} va con {numeros}")

