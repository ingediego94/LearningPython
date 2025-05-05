# Construir un programa que simule el funcionamiento de una calculadora que puede realizar las cuatro operaciones aritmeticas básicas (suma, resta, multiplicacion y division). El usuario debe especificar la operacion con el primer caracter del nombre de la operacion.
    # S, s = suma
    # R, r = resta
    # D, d = division
    # P, p, M, m = multiplicacion

# Peticion de numeros

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))


# Selecion de operacion
operacion = input("Escoja la operacion a realizar: \n S = para suma. \n R = para resta. \n P o M = para multiplicacion.\n D = para division. ").upper()


# Operaciones
suma = (num1 + num2)
resta = (num1 - num2)
multiplicacion = (num1 * num2)
division =  (num1 / num2)

# Impresion de la operacion
if operacion == 'S':
    print(f"El resultado es: {suma}" ) 
elif operacion == 'R':
    print(f"El resultado es: {resta}" )
elif operacion == 'P' or operacion == 'M':
    print(f"El resultado es: {multiplicacion}" )
elif operacion == 'D':
    print(f"El resultado es: {division:.2f}")
else:
    print("Ha escogido una opcion incorrecta.")
