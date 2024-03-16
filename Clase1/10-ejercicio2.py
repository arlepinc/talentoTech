# CICLO WHILE

import random

numeroSecreto = random.randint(1,10)
adivinanza = None
intentos = 0


while adivinanza != numeroSecreto:
    adivinanza = int(input("ADIVINA EL NUMERO ENTRE 1 a 10"))
    intentos = intentos + 1

print(f"PERFECTO, ADIVINASTE EL NUMERO ES{numeroSecreto} lo lograste en {intentos} intentos")
