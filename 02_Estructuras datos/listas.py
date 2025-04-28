# LISTAS
## Estructura de datos flexible
mi_lista = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 40, 3.1416, [1,2,3], True]

print(mi_lista[0])

print(mi_lista[-1])

print(mi_lista[1:3])

print(mi_lista[:3])

print(mi_lista[2:])

print(mi_lista)

print(mi_lista[:])


# Cuenta la cantidad de elementos que tiene la lista
print(len(mi_lista))    


# Inserta un elemento al final de la lista
mi_lista.append('Hola')     


# Insertar un elemento en una posicion deseada
mi_lista.insert(2, 'Cadena texto')      #Inserta el texto 'Cadena ..' en la posicion 3 de la lista

print(mi_lista)


# Inserta varios elementos al final de la lista
mi_lista.extend([4, 5, 6, 10])      

print(mi_lista)

lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = lista1 + lista2
print(lista3)       # Se pueden sumar dos listas


# Saber si un determinado elemento se encuentra en la lista
print(3 in lista1)      # Un elemento se encuentra dentro de la lista
print('Diego' in lista2)    # 'Diego' se encuentra en la lista2 ?


# Saber en que posicion se encuentra un determinado elemento
print( lista3.index(6))  



lista = [1,2]

# Añade un elemento al final
lista.append(3)

# Agrega n elementos a la lista al final
lista.extend([4,5,7,"DJ"])

# Agrega un nuevo elemento a la lista en la posición indicada
lista.insert(5,6)

# Elimina el elemento indicado, en la primera posicion que lo encuentre.
# Usa el valor de la lista
lista.remove("DJ")

# Elimina el elemento en la posición indicada. Permite extraer ese valor a otra variable. 
# Usa el índice. 
lista.pop(1)
nuevo = lista.pop(1)

lista.count(5)

lista.reverse()

lista.sort()

lista.sort(reverse=True)

lista.clear()   


print(f"Elementos de la lista: {lista}")

