# Ejercicio 2: DISCORD Convertir salario de COP a USD
#Descripción:
#Escribe una función llamada convertir_a_usd que reciba dos parámetros:
    #salario_cop (float): el salario en pesos colombianos.
    #tasa (float): la tasa de conversión de pesos a dólares.
#La función debe devolver el valor del salario convertido a dólares, 
# utilizando la fórmula: salario_usd = salario_cop / tasa
#Ejemplo:
#convertir_a_usd(5000000, 4000) → 1250.0

def convertir_a_usd(salario_cop, tasa):
    salario_usd = salario_cop / tasa
    return salario_usd

print("=" * 50)
print("||         CONVERSOR DE DIVISAS EL RIWI        ||")
print("=" * 50)


pesosCol = float(input("Escribe la cantidad en COP a convertir a USD: \n\t"))

tasaCop = float(input("Ingresa la TRM de hoy: \n\t"))

dolares = convertir_a_usd(pesosCol, tasaCop)

print(" - " * 17)
print("             RESULTADO CONVERSION         ")
print(f"Los ${pesosCol} a una tasa de ${tasaCop}, representan \nhoy en la TRM ${round(dolares, 2)} USD.")
print(" - " * 17)
print()
print("=" * 50)