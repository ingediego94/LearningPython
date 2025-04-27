# CONDICIONALES COMBINADOS

edad = int(input("Digita tu edad: "))

#if edad > 0 and edad < 100:     # Condicional combinado.
if 0 < edad < 100:  # Esto es exactamente lo mismo que la linea de arriba
    print("Edad correcta.")
    if edad >= 18:          # Codicional anidado: un if dentro de otro.
        print("Es mayor de edad.")
else:
    print("Edad incorrecta.")