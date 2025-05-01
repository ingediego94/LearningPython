#  Tabla de multiplicar con while

#    Pide un número al usuario y usa while para mostrar su tabla de multiplicar del 1 al 10.

tries = 0

while True:

    try:

        number = int(input("Ingresa un número: "))

        i = 1

        if number <= 0:
            raise ValueError("El numero debe ser mayor a 0.")

        while i != 11:
            print(f"{number} x {i} = {number*i}")
            i += 1

        tries += 1

        if tries == 1:
            print("Levas ", tries, " tabla de multiplicar.")
        else:
            print("Levas ", tries, " tablas de multiplicar.")

    except ValueError as e:
        print(e) 

