nombreCompleto = "Carlos Andres Borbón"

# FOR CON RANGE:

# range(final)   Imprime los números desde el 0 hasta el final-1
for i in range(5):
    print(i)

print("-" * 10)

# range(inicio, final)      Genera numeros desde el inicio hasta el final-1
for i in range(2, 6):
    print(i)

print("-" * 10)

# range(inicio, final, salto)   Genera desde el inicio hasta el final-1 haciendo saltos determinados
for i in range(1, 10, 2):
    print(i)

print("=" * 10)


# FOR CON LISTAS:
# Aqui el bucle recorre cada posicion de la lista imprimiendo uno por uno

frutas = ["pera", "manzana", "piña"]

for fruta in frutas:
    print(fruta)


print("=" * 10)

# FOR CON TUPLES:
# Aqui hace lo mismo que cuando recorre una lista

ciudades = ("New York", "Medellín", "Sidney", "Hong Kong")

for ciudad in ciudades:
    print(ciudad)

print("=" * 10)

# FOR CON CADENA DE CARACTERES:
# Imprime caracter por caracter de la cadena de texto

mensaje = "Hola mundo"

for caracter in mensaje:
    print(caracter)