
# Pedimos al usuario que ingrese números separados por comas
entrada = input("Ingresa varios números separados por comas: ")

# Dividimos el string en una lista de textos usando split(',')
lista_texto = entrada.split(",")

# Convertimos cada texto en número (int o float)
lista_numeros = [int(num.strip()) for num in lista_texto]

# Mostramos la lista final
print(lista_numeros)
