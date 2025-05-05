reb = 0
noreb = 0

for i in range(8):
    resultado = int(input("Ingresa el resultado de la venta, 1 si fue mayor a 200, 2 si fue menor.\n"))

    if resultado == 1:
        reb += 1
    elif resultado == 2:
        noreb += 1

print("La cantidad de clientes que rebasaron fue de: ", reb)
print("La cantidad de clientes que no rebasaron fue de: ", noreb)

if reb > 4: 
    print("Se da premio.")