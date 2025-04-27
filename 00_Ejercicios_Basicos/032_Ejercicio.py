#  solicita al usuario ingresar la base y la altura de un rectángulo para calcular el área. Al inicio, el programa tiene las siguientes tres líneas

base = float(input("Ingresa la base del rectangulo: \n"))

altura = float(input("Ingresa la altura del rectangulo: \n"))

area_rect = base * altura

print(f"El área del rectángulo es: {round(area_rect, 2)}")