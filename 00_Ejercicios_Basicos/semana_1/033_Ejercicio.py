
suma_tot = 0
contador_clientes = 0

consumo = float(input("Ingresa el consumo, -1 para finalizar."))

while consumo != -1:
    suma_tot += consumo
    contador_clientes += 1
    consumo=float(input("Ingresa el consumo, -1 para finalizar"))

if consumo != 0:
    consumo_prom = suma_tot / contador_clientes
    print(f"La venta promedio es de {consumo_prom:.2f}")
else:
    print("No hubo consumidores.")