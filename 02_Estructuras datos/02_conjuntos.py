# CONJUNTOS
# Coleccion de elementos no ordenados - DESORDENADOS
# Heterogeneo pero solo con elementos inmutables
# Mutable
# Sin repeticion - NO PUEDE TENER VALORES DUPLICADOS
# No permite coleeciones dentro de el (no permite contener listas o tuplas)
# se crea con: set()
# Los conjuntos y diccionarios ambos se crean con {} por eso toca especificar con set() que será un conjunto

#       conjunto = set()    Especificamos que sera un conjunto
#       conjunto = {}       Especificamos que está vacio el conjunto

# Conjunto vacio:
conjuntoVacio = set()


# conjunto con una lista:
print("Conjunto con una lista: ")
print(set([5, 2, 3, 8, 11]))

# conjunto con una tupla
print("Conjunto con una tupla: ")
print(set((23, 15, 5, 8, 93)))

# conjunto con un string. Si usamos un string, tendremos es un conjuto de char porque es una lista de caracteres
print("Conjunto de string: ")
print(set("Hola mundo"))    #imprime los caracteres en desorden

# uno de sus usos es eliminar elementos repetidos de la secuencia
conjunto = set([2, 3, 3, 4, 9])
print("Conocer los elementos del conjunto sin contar repetidos: ")
print("Conjunto: " , conjunto)      # no cuenta al 3 dos veces.



# Métodos
# .add  = agregar elemento
conjunto.add(1)
print("Se agrega el elemento 1: " , conjunto)

# .remove   = eliminar elemento
conjunto.remove(2)
print("Elimina el elemento 2: " , conjunto)
conjunto.discard(1)     # tambien remueve elementos del conjunto

# Vacía por completo el conjunto
print(conjunto.clear())

# Busca un elemento dentro del conjunto
print(3 in conjunto)        # Busca si el 3 está dentro del conjunto y retorna un bool

# Busca si un elemento no está dentro del conjunto
print(3 not in conjunto)        # Busca si el 3 está dentro del conjunto y retorna un bool

# Podemos realizar operacines de conjuntos
conjunto2 = set([5, 3, 5, 6])
conjunto3 = set([4, 9])

print("Imprime los tres conjuntos" , conjunto, conjunto2, conjunto3)

# .intersection  =  podemos conocer la interseccion de los conjutos. Elementos en comun

# interseccion entre conjunto y conjunto 2
print("Muestra la interseccion de conjunto y conjunto2: ")
print(conjunto.intersection(conjunto2))


# .issubset  = comprobar si los elementos de un conjunto estan incluidos en otro. Es decir que la totalidad de un conjunto está dentro del otro.

# Los elementos de conjunto2 no estan incluidos en conjunto
print("Los elementos de conjunto2 están incluidos en conjunto? ")
print(conjunto2.issubset(conjunto))     # retorna false

# Los elementos de conjunto 
print("Los elementos de conjunto3 estan incluidos en conjunto? ")  # Todos los emementos de conjunto3 están dentro de conjunto?
print(conjunto3.issubset(conjunto))

# ------------------------------

# OPERADORES DE CONJUNTOS:
    # conj1 | conj2     = Union
    # conj1 - conj2     = Diferencia: 
    # conj1 >= conj2    = Superconjunto
    # conj1 & conj2     = Interseccion
    # conj1 ^ conj2     = Diferencia simetrica: elementos que diferencian a DOS conjuntos
    # conj1 <= conj2    = Subconjunto

colores1 = set(["Negro", "Blanco", "Naranja", "Rojo", "Azul"])
colores2 = set(["Negro", "Gris", "Verde", "Rojo", "Azul claro"]) 
# Union |
print("Unión: " , colores1, colores2)

# Interseccion &
print("Interseccion: " , colores1 & colores2)

# Diferencia -
print("Diferencia: " , colores1 - colores2)

# Superconjunto >=
print("Superconjunto: " , colores1 >= colores2)
print("porque colores1 no tiene todos los colores que tiene colores2.\n")

# Diferencia simetrica: elementos que diferencian a DOS conjuntos
print("Diferencia simétrica: " , colores1 ^ colores2)

# Subconjunto <=
print("Subconjunto: " , colores1 <= colores2)


print("------------------------")
a = {1, 2, 3}
b = {3, 2, 1}

# Validamos si tienen los mismos elementos ('a' es igual a 'b') sin importar el orden.
print(a == b)
