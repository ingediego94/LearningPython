# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.

montoDinero = float(input("Cuando dinero dispones en tu cuenta? \n"))

interes = 0.04

year1 = (montoDinero * interes) + montoDinero

year2 = (year1 * interes) + year1

year3 = (year2 * interes) + year2

print(f"To monto total es de: {round(year1, 2)} para el año 1.")
print(f"To monto total es de: {round(year2, 2)} para el año 2.")
print(f"To monto total es de: {round(year3, 2)} para el año 3.")