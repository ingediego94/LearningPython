# Escribir un programa que pregunte por una muestra de numeros separados por comas, los guarde en una lista y muestre por pantalla su media (promedio) y la desviación estandard

import math

vecMuestras = []
total = 0
muestras = int(input("Cuantas muestras vas ha introducir? \n"))
varianza = 0
x = 0

for i in range(muestras):
    muestra = float(input("Cual es la muestra " + str(i + 1) + "?\n"))
    vecMuestras.append(muestra)

for j in vecMuestras:
    total += j

media = total / len(vecMuestras)

for k in vecMuestras:
    x += (k-media)**2

varianza = x / (len(vecMuestras)-1)

desviacion = round( math.sqrt(varianza) ,2)

print(f"La media es: {str(media)}, y la desviación es {str(desviacion)}")