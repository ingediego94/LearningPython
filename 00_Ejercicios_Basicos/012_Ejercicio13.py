# Crear dos conjuntos vacios y pedirle al usuario llenar cada uno de ellos con la cantidad de elementos que desee. Luego mostrar por pantalla que elementos tiene cada conjunto, su interseccion, su union,  

conjunto1 = set()
conjunto2 = set()


try:

    opcion1 = int(input("Cuantos datos va a ingresar en el conjunto 1?\n "))

    opcion2 = int(input("Cuantos datos va a ingresar en el conjunto 2?\n"))

    i = 0
    j = 0

    while i < opcion1:
        conjunto1.add(int(input(f"Conjunto 1 --> Ingresa el elemento {i+1} de {opcion1} y pulsa enter: \n")))
        i = i+1

    while j < opcion2:
        conjunto2.add(int(input(f"Conjunto 2 --> Ingresa el elemento {j+1} de {opcion2} y pulsa enter: \n")))
        j = j+1

    print(f"Elementos del conjunto 1: {conjunto1}")
    print(f"Elementos del conjunto 2: {conjunto2}")

    # OPERACIONES CON CONJUNTOS
    union = conjunto1 | conjunto2 
    interseccion = conjunto1 & conjunto2
    diferencia1y2 = conjunto1 - conjunto2   # Elementos de 1 que no están en 2
    diferencia2y1 = conjunto2 - conjunto1   # Elementos de 2 que no están en 1
    dif_simetrica = conjunto1 ^ conjunto2   # Elementos que están en 1 y 2 pero no están en ambos.
    subconjunto1 = conjunto1.issubset(conjunto2)     # El conjunto 1 es un subconjunto de conj. 2?
    subconjunto2 = conjunto2.issubset(conjunto1)     # El conjunto 2 es un subconjunto del con. 1?
    superconjunto = conjunto1.issuperset(conjunto2)    # Superconjunto: El conjunto 1 es un superconjunto que engloba al conjunto 2?
    disconexo = conjunto1.isdisjoint(conjunto2)

    # HACER UN CONJUNTO INMUTABLE:
    # no se puede editar, modificar, agregar
    # conjuntoInmutable = fronzenset({1,2,3})

    # El conjunto 1 es disconexo del conj. 2?   a que no comparten ningun elemento en común

    print(f"Los conjuntos son iguales? Rta: {conjunto1 == conjunto2}")

    print(f"La unión de los dos conjuntos es: {union}")
    print(f"La intersección de los dos conjuntos es: {interseccion}")
    print(f"La diferencia del conjunto 1 y el conjunto 2 es: {diferencia1y2}")
    print(f"La diferencia del conjunto 2 y el conjunto 1 es:{diferencia2y1}")
    print(f"La diferencia simétrica de los conjuntos 1 y 2 es:{dif_simetrica}")
    print(f"El conjunto 1 es un subconjunto del conjunto 2? {subconjunto1}")
    print(f"El conjunto 2 es un subconjunto del conjunto 1? {subconjunto2}")
    print(f"El conjunto 1 es un superconjunto que engloba al conj. 2? {superconjunto}")
    print(f"El conjunto 1 es un disconexo del conjunto 2? {disconexo}")

except:
    print("Error. Ingrese datos numericos.")





