# Para eliminar elementos de una lista podemos usar remove(), del 

lista1 = [1,2,3,4,5,4,6,7,8,9,10,11]
print(lista1)


# REMOVE elimina solo el primer registro que aparece.
lista1.remove(4)
print(lista1)


# DEL elimina multiples elementos e incluso la lista completa
    # Elimina la 10ma posicion que es '11'
del lista1[10]
print(lista1)

    # Elimina del inidice 1 al 3
del lista1[1:3]
print(lista1)

    # Elimina toda la lista
del lista1
print(lista1)   # No se puede imprimir porque ya no existe
