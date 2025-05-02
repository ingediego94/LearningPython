numero = int(input("Ingresa un número: "))

for i in range(2, numero):
    if numero % i == 0:
        print(f"{numero} no es primo.")
        break
else:
    print(f"{numero} es primo.")
    

'''
Sentencias de Control de Bucles

Puedes controlar el flujo de los bucles con:

    break: Sale del bucle inmediatamente.
    continue: Omite el resto de la iteración actual y pasa a la siguiente.
    else: Se ejecuta cuando el bucle termina normalmente (es decir, sin encontrar un break).

'''