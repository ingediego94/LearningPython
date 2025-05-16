# Declaracion funcion lambda suma
suma = lambda a, b : a + b

print(suma(10,30))


# Lambda elevando al cuadrado
cuadrado = lambda c, d: c ** d

resultado1 = cuadrado(3,2)
print(resultado1)


# Lambda con lista para sumar los numeros
suma_lista = lambda lista: sum(lista)

lista_numeros = [1,2,3,4,5,6,7,8,9,10]
print(suma_lista(lista_numeros))


# Lambda para filtrar pares de una lista
    # Qué hace: pasa cada número a la función lambda. Si el resultado es True (x % 2 == 0), el número se mantiene.
    #Uso: útil para filtrar elementos de una lista que cumplan una condición (en este caso, números pares).
filtrar_pares = list(filter(lambda lista_x : lista_x % 2 == 0, lista_numeros))
print(filtrar_pares)


# Lambda para multiplicar cada numero de la lista x 10
multiplicados = list(map(lambda x: x * 10, lista_numeros))
print(multiplicados)


# Ordenar una lista de tuplas por el segundo valor
tuplas = [(1, 3), (2, 1), (4, 2)]
ordenadas = sorted(tuplas, key=lambda x: x[1])
print(ordenadas) 
