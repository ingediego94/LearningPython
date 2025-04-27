# Hacer un programa que pida 2 numeros y se de cuenta cual de ellos es par, o si ambos lo son.

numero1 = int(input("Ingresa un numero: "))

numero2 = int(input("Ingresa otro numero: "))

if numero1 % 2 == 0 and numero2 % 2 == 0:
    print(f"Ambos números ({numero1} - {numero2}) son pares. ")
elif numero1 % 2 == 0 and numero2 % 2 !=0:
    print(f"Solo el primer numero ({numero1}) es par.")
elif numero1 % 2 != 0 and numero2 % 2 == 0:
    print(f"Solo el 2do numero ({numero2}) es par.")
else:
    print("Ninugno de los números es par.")
