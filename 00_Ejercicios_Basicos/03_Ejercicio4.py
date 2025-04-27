# Progama para ingresar el radio del circulo y se reporte el área del circulo y la longitud de la circunferencia.

import math

radio = float(input("Ingrese el radio del circulo: "))

area = round(math.pi * (radio**2), 2)

longitud = 2 * math.pi * radio


print(f"El área del circulo es: {area}, y la longitud de su circunferencia es: {longitud:.3f}")
# con el   variable:.3f     le estamos diciendo que a la variable le muestre solo tres decimales.