# LISTA
# Es una secuencia de datos ordenados. 
    # La posición importa. 
    # Heterogenea : puede contener distintos tipos de datos.
    # Mutable: Podemos modificar la secuencia: modificando, eliminando o añadiendo elem.
    # Se usan corchetes []

# esto es una lista
lista = [23, True, 3.1416, "Cadena de texto", 5.231]
# Nos imprimirá el primer elemento
print(lista[0])
# Imprime solo el indice especificado de la lista
print("Este es el 2do elem. de la lista: " , lista[2])

# Imprimirá el último elemento de la lista
print(f"El último elemento de la lista es: {lista[-1]}")
print(f"El penúltimo elemento de la lista es: {lista[-2]}")

# Obtener una sublista a partir de dos índices (desde el primer elemento solicitado, hasta el anterior al segundo(4))
print("La sublista es: " , lista[2:4])

# Le estamos pidiendo solo los datos desde el inicio hasta el 4to elemento, es decir uno antes del especificado, es decir el índice 3   [:4]
print("La lista desde el inicio hasta el 3er elem. es: " , lista[:4])

# Le podemos especificar que la imprima desde un elemento inicial hasta el final
print("La lista desde el 2do elemento es: " , lista[1:])

# Imprime toda la lista [:]
print("La totalidad de la lista es: " , lista[:])

# Imprime toda la lista también
print("TAmbién imprime toda la lista: " , lista)

# cambiar un elemento (True) por otro en su posicion
lista[1] = False 
print(lista)

# conocer la longitud de una lista  .len()
print("Longitud de la lista:" , len(lista), "Elementos")

#insertar un nuevo elemento en la posicion 3, incluso otra lista dentro de la lista
lista[2] = [3,2,1]
# imprimer la lista actualizada
print(f"Ahora la lista es: {lista}")

# Agregar otro elemento a la lista (otra forma):
# Con este podemos agregar el dato en el posicion que queramos
lista.insert(6, "OtroValor")    # primero va el indice y luego el valor a insertar

print("--------------------")




# -----------------------------------------
# Metodos dentro de las listas
listaNueva = [1, 2, 3, 4, 5, 6, 2]
print(listaNueva)

# 2) .append  Para agregar un elemento al final
listaNueva.append("NuevoElemento")
print(listaNueva)

# Para agregar varios elementos al final de la lista
lista.extend([20, "otro", True, "3,2"])

# 2) .count para contar el numero de veces que se repite un elemento
print(listaNueva.count(2))

# 3) .index  Devuelve la primer posición de aparición de un elemento
print(listaNueva.index(5)) #Aqui estamos buscando el número 5

# 4) .remove  Elimina la primer aparición de un elemento como valor, mas no como indice
print(listaNueva.remove(2))

# Elimina el índice que le especifiquemos de la lista
print(lista.pop(2))     #buscaría ese indice y lo eliminaria

# Elimina el último elemento de toda la lista
print(lista.pop())

# Eliminar o vaciar por completo la lista
print(lista.clear())

# Sumar una lista a otra
lista3 = lista + listaNueva
print(f"La lista 3 contiene la suma de la 1 y la 2 así: \n {lista3}")

# Saber si un valor esta dentro de los elementos de una lista
print(f"El valor de 'otro' está en la lista final?" , "otro" in lista3)

# invertir el orden de la lista
print(lista.reverse())

# Duplicar los elementos de la lista
#   lista = [1,2,3,4,True, "no"] *2
# Quintuplicar los elementos de la lista
#   lista = [1,2,3,4,True, "no"] *5

# Ordenar los elementos de una lista (enteros) de manera ascendente menor a mayor
#   lista = [89, 34, 2, 3, 54, 10, 5, 1]
#   lista.sort()

# Ordenar los elementos de una lista (enteros) de manera descendente mayor a menor
#   lista = [89, 34, 2, 3, 54, 10, 5, 1]
#   lista.sort(reverse=True)