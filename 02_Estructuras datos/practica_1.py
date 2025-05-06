
# METODOS PARA USAR CON LISTAS

lista1 = [1,23,99,5,-1,8,9,10]
lista2 = [2,4,9,99]

# SUMAR una lista a otra
lista3 = lista1 + lista2

# Ordenar una lista
lista3.sort()
print(lista3)

# Agregar un elemento al final de la lista
lista3.append(45)
print(lista3)

# Agregar varios elementos a la vez en la lista
lista3.extend([-3,88,100,99])
print(lista3)

# Insertar un valor en una posicion específica
lista3.insert(1,0)
print(lista3)

# Remover un valor específico de la lista. Solo elimina el primer encontrado
lista3.remove(9)
print(lista3)

# Retorna el indice de la primera poscion donde fue encontrado
posicion = lista3.index(8)
print(posicion)

# Cuenta la cantidad de elementos que tiene la lista
cant_De_99 = lista3.count(99)
print(cant_De_99)

# Invierte la lista
lista3.reverse()
print(lista3)

# Copiar una lista, si modifico lo valores estos no cambiaran
lista4 = lista3.copy()
lista3.append(200)
print(lista3)
print(lista4)

# Eliminar un elemento y guardarlo en otra variable 
eliminado = lista3.pop(-1)
print(eliminado)
print(lista3)

# Eliminar un solo elemento (funciona a base del indice)
del lista3[0]
print(lista3)

# Elimina varios elementos a la vez. (Elimina desde la posicion 1 a la 5, porque cuenta
# el ultimo numero -1)
del lista3[1:6]
print(lista3)

# Vaciar por completo la lista
lista3.clear()
print(lista3)