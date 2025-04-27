# Hacer un programa que pida un caracter e indique si es una vocal o no.

texto = input("Ingrese un caracter: ").lower()      # Transforma el texto a minuscula
# .upper() transforma el texto a mayuscula

# texto.lower() nos estaría retornando una copia, no afectaria a la variable texto.

if texto == 'a' or texto == 'e' or texto == 'i' or texto == 'o' or texto == 'u':
    print(f"El caracter es una vocal: {texto}")
else:
    print("El caracter es una consonante.")