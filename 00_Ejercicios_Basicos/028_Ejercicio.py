# Usa for para calcular el consumo promedio de los siguientes clientes.

listado = [130, 85, 210, 45, 153, 78.5, 264.5, 94]

suma = 0
clientes =0

for consumo in listado:
    suma = suma + consumo
    clientes = clientes + 1

print(suma / clientes)

