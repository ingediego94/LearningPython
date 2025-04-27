#  Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.
num1 = int(input("Ingrese un numero entero: \n"))
num2 = int(input("Ingrese otro numero entero: \n"))

cociente = num1 // num2

resto = num1 % num2

print(f"El cociente de {num1} / {num2} es: {cociente}")

print(f"El residuo de {num1} entre {num2} es: {resto}")
