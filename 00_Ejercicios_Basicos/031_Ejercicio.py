# Crear un programa que pida un entero y lo verifique para ver si es multiplo de 3

numero =int(input("Ingrese un numero: \n"))

if numero % 3 == 0:
    print(f"{numero} si es multiplo de tres.")
else:
    print(f"{numero} no es multiplo de tres.")