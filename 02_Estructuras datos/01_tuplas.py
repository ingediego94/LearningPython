# TUPLAS
# Secuencia de datos:
    # Ordenada,
    # Heterogenea,
    # Inmutable: no se puede modificar una vez creada.
    # Se escribe con parentesis
    # para acceder a uno de sus elementos es con []
    # Las tuplas solo sirven para buscar elementos
    # LAs tuplas son mucho mas rapidas que las listas

miTupla = ("Este es un texto", 123, False, [1,245,3], 123)
print(miTupla)

# Muestra el elemento que le indiquemos su indice
print(miTupla[3])
# Que nos muestre desde el 2do elemento hasta el final
print(miTupla[1:])



# Buscar elementos dentro de las tuplas
print(123 in miTupla)


# Metodos en las tuplas

# .count  = devuelve cuantas veces aparace un elemento. 
print(miTupla.count(123))

# .index  = devuelve la posicion de lo que le pedimos (si hay mas de un elemento igual, nos mostrará solo el 1ero de ellos)
print(miTupla.index(False))

# nos cuenta que longitud (cuantos elementos) tiene en total a tupla
print(len(miTupla))

# Podemos transformar una tupla en lista:
lista = list(miTupla)
print(type(lista))

# Podemos convertir una lista en tupla
listaPrueba = [1,2,3,4,'No']
tuplaPrueba = tuple(listaPrueba)
print(type(tuplaPrueba))