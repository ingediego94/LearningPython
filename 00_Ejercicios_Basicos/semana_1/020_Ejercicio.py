# Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.

nombre = input("Cual es tu nombre? \n").upper()

numero = int(input("Ingresa un numero entero: \n"))

i=0

#while i < numero:
#    print(f"Mi nombre es: {nombre}")
#    numero = numero -1

print(f"{(nombre)} \n" * numero)
