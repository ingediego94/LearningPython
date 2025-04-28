
numeros = [3, 8, 9, 15, 1, 22, 7, 18]
umbral = 10

for numero in numeros:
    if numero > umbral:
        print(f"El primer número mayor que {umbral} es {numero}.")
        break
    else:
        print(f"Ningún número en la lista es mayor que {umbral}.")