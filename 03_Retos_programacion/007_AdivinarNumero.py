# 1. Adivina el número
# El programa debe tener un número secreto (por ejemplo, 7). Pide al usuario que adivine el número hasta que lo acierte.

numeroSecreto = 23

while True:
    
    try:
        
        entrada = int(input("Ingresa un numero: "))
        
        break
    
    except ValueError as e:
        print("Error: ", e)
        print("Intenta nuevamente. \n")

while entrada != numeroSecreto:
    
    if entrada > numeroSecreto:
        print(f"El número secreto es mayor que {numeroSecreto}.")
    elif entrada < numeroSecreto:
        print(f"El número secreto es menor que {numeroSecreto}.")

if entrada == numeroSecreto:
    print("Felicidades, has acertado.")