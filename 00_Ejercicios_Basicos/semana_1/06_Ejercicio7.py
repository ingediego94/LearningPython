# Hacer un programa que pida 3 numeros y determine cual es el mayor.

# Petición de los 3 numeros.
num1 = int(input("Ingresa el primer número."))
num2 = int(input("Ingresa el segundo número."))
num3 = int(input("Ingresa el terce número."))

# Determinacion de cual de ellos es mayor.

if num1 >= num2 and num2 >= num3:
    print(f"El número {num1} es el mayor de los tres.")
elif num2 >= num1 and num2 >= num3:
    print(f"El número {num2} es el mayor de los tres.")
elif num3 >= num1 and num3 >= num2:
    print(f"El número {num3} es el mayor de los tres.")


