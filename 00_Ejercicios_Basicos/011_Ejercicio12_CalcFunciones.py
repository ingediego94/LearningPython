
# crea una calculadora basica por medio de funciones

#estado = input("Desea realizar una operacion?").upper()



# Peticion de numeros por consola
num1 = float(input("Ingresa el primer número: \n"))
num2 = float(input("Ingresa el otro número: \n"))

# DEFINICON DE FUNCIONES

# Suma
def suma(a, b):
    resultado = a + b
    return resultado

# Resta
def resta(a, b):
    resultado = a -b
    return resultado

# Multiplicacion
def multiplicacion (a, b):
    resultado = a * b
    return resultado

# Division
def division (a, b):
    resultado = a / b
    return resultado

# Exponenciacion
def exponenciacion(a, b):
    resultado = a ** b
    return resultado

# Raíz n esima
def raiz(a, b):
    resultado = a ** (1/b)
    return resultado



# Seleccion de operaciones
print("Seleccione la operacion que desea realizar: ")

opcion = input(" 1 o S = Para Suma.\n 2 o R = Para resta.\n 3 o M = ParaMultiplicacion.\n 4 o D = Para Division. \n 5 o E = Para Exponenciacion.\n 6 oZ = Raiz.\n").upper()

if opcion == '1' or opcion == 'S':
    print(f"El resultado de {num1} + {num2} es: {suma(num1, num2)}.")
elif opcion == '2' or opcion == 'R':
    print(f"El resultado de {num1} - {num2} es: {resta(num1, num2)}.")
elif opcion == '3' or opcion == 'M':
    print(f"El resultado de {num1} * {num2} es: {multiplicacion(num1, num2)}.")
elif opcion == '4' or opcion == 'D':
    print(f"El resultado de {num1} / {num2} es: {division(num1, num2)}.")
elif opcion == '5' or opcion == 'E':
    print(f"El resultado de {num1} ^ {num2} es: {exponenciacion(num1, num2)}.")
elif opcion == '6' or opcion == 'Z':
    print(f"El resultado de la raíz {num2}esima de {num1} es: {raiz(num1,num2):.4f}.")
else:
    print("Error. \nOpcion incorrecta.")



