# Hacer un programa que simule un cajero automático con un saldo inicial de $1000 y tendrá el siguiente menu de opciones.
#   1. Ingresar dinero en la cuenta
#   2. Retirar dinero de la cuenta.
#   3. Mostrar dinero disponible.
#   4. Salir

saldo = 1000
retiro = 0
ingreso = 0

print("Bievenido a su red de cajeros DV-Bank.")

seleccion = int(input("Seleccione la operacion que desea realizar:\n 1) Ingresar dinero. \n 2) Retirar dinero de la cuenta. \n 3) Mostrar dinero disponible. \n 4) Salir"))

if seleccion == 1:
    ingreso = float(input("Cuanto dinero desea ingresar a su cuenta? "))
    saldo = saldo + ingreso
    print(f"Su nuevo saldo es de: ${saldo}")
elif seleccion == 2:
    retiro = float(input("Cuanto dinero desea retirar? "))
    if retiro > saldo:
        print(f"No dispone de tanto dinero, solo cuenta con {saldo} y no con {retiro}")
    else:
        saldo -= retiro
        print(f"Su nuevo saldo es de: ${saldo}")
elif seleccion == 3:
    print(f"Dispone de un total de: {saldo}")
elif seleccion == 4:
    print("Gracias por utilizar nuestros servicios.")
else:
    print("Error. Ha escogido una opcion incorrecta.")