num1 = float(input("Ingresa un numero: "))

num2 = float(input("Ingresa otro numero: "))

operacion = input("Ingresa la operacion a desarrollar:\n S o s= Suma. \n R o r= Resta. \n D o d= Division. \n M o m= Multiplicacion.").lower()

def suma(num1, num2):
    adicion = num1 + num2
    print(f"La suma es: {adicion}")

def resta(num1, num2):
    diferencia = num1 - num2
    print(f"La resta es: {diferencia}")

def multiplicacion(num1, num2):
    multi = num1 * num2
    print(f"El producto es: {multi}")

def division(num1, num2):
    div = num1 / num2
    print(f"El resultado es: {div}")

if operacion == "s":
    suma(num1, num2)
elif operacion == "r":
    resta(num1, num2)
elif operacion == "m":
    multiplicacion(num1, num2)
elif operacion == "d":
    division(num1, num2)
else:
    print("Se ha presentado un error.")
