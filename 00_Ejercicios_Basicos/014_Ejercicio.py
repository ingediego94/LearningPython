# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.

try:
    peso = float(input("Ingrese su peso en Kg.\n"))

    estatura = float(input("Ingrese su estatura en en metros \n"))

    imc = peso / estatura**2

    if peso > 0 and estatura > 0:

        if imc < 18.5:
            print(f"Su IMC es de de: {round(imc, 2)}, es decir está en DELGADEZ.")
        elif imc >= 18.5 or imc <= 24.9:
            print(f"Su IMC es de de: {round(imc, 2)}, es decir está en NORMAL.")
        elif imc >= 25 or imc <= 29.9:
            print(f"Su IMC es de de: {round(imc, 2)}, es decir está en SOBREPESO.")
        elif imc >= 30 or imc <= 34.9:
            print(f"Su IMC es de de: {round(imc, 2)}, es decir está en OBESIDAD 1.")
        elif imc >= 35 or imc <= 39.9:
            print(f"Su IMC es de de: {round(imc, 2)}, es decir está en OBESIDAD 2.")
        else:
            print(f"Su IMC es de de: {round(imc, 2)}, es decir está en OBESIDAD 3.")

    else:
        print("Datos erroneos, intente de nuevo.")

except:
    print("Error, vuelva a intentarlo.")
