# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.


cantidad = float(input("Que cantidad desea invertir? \n"))

interes = float(input("Cual es la tasa de interés anual (TEA)? \n"))

anos = int(input("Cual es su plazo de inversión en años? \n"))


print("Error, los valores ingresados son erroneos, intente nuevamente.")


ganancia = cantidad * (interes/100+1) ** anos

print(f"La ganancia obtenida durante los {anos} fue de {round(ganancia,2)}")

# print(f"La ganancia en solo intereses fue de {}")