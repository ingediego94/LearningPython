puntuacion = int(input("Ingresa tu puntuación (0-100): "))

if puntuacion >= 60:
    print("¡Aprobaste!")
    if puntuacion >= 90:
        print("¡Wow, obtuviste una A!")
    elif puntuacion >= 80:
        print("¡Bien, obtuviste una B!")
else:
    print("Reprobaste. ¡Estudia más!")