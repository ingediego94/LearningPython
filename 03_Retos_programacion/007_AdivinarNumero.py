# 1. Adivina el número
# El programa debe tener un número secreto (por ejemplo, 7). 
# Pide al usuario que adivine el número hasta que lo acierte.

# Importamos libreria para numeros aleatorios
import random as rd


# Numero secreto que tienen que adivinar
secretNumber = rd.randint(0, 999)

# Bucle infito para solicitar un numero valido (no str)
while True:
    
    try:
        
        entryNumber = int(input("Ingresa un numero: "))

        if entryNumber > secretNumber:
            print(f"El número a adivinar es menor. Intenta de nuevo.")            
                    
        elif entryNumber < secretNumber:
            print(f"El número a adivinar es mayor. Intenta de nuevo.")

        else:
            print("Felicidades, has acertado.")
            break
    
    except ValueError as e:
        print("Error: ", e)
        print("Intenta nuevamente. \n")
 
   

