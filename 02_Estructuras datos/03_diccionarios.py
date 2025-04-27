# DICCIONARIOS
# Un diccionario permite relacionar pares de elementos clave - valor
# la clave key nos sirve para buscar e identificar el elemento con el que tiene relacion
# {key : value}
    # No tiene orden.
    # Heterogeneo con clave inmutable
    # Mutable
    # Se usan llaves  {}

diccionario = {1:"Uno", 2:"Dos", 3:"Tres"}
print(diccionario)

# Le agregamos un nuevo elemento
diccionario[4] = "CUATRO"
print(diccionario)

# Otra forma de crear diccionarios
dict_lista_tuplas = dict([(1,"Mazda"), (2,"Chevy"), (3,"Renoult")])
print(dict_lista_tuplas)

# Si las claves son de tipo string, se puede introducir directamente separado por comas las claves seguidas de su valor
dict_lista_string = dict(Uno = 1, Dos = 2, Tres = 3)
print(dict_lista_string)

# Se puede usar cualquier tipo de datos como value pero el key al usarse como valor debe ser inmutable
dict_tipos = {1:"integer", 2.2:"float", "texto":"string", (1,2):"tupla"}
print(dict_tipos)

# El key no debe repetirse, en caso de hacerlo, tomará solo el valor de la ultima repeticion
dict_repeticion = {1:"Primero", 1:"Ultimo"}
print(dict_repeticion)


# Metodos

# .keys()   devuelve una lista con las claves
print("Las claves de diccionario son: " , diccionario.keys())

# .values()     devuelve una lista con los valores
print("Los valores de diccionario son: " , diccionario.values())

# .items()      devuelve una lista de tuplas con los pares de datos key:value
print("La lista de tuplas con los pares de datos key:value de diccionario es: \n" , diccionario.items())

# Todos estos metodos devuelven vistas dinamicas, es decir, si se guarda la lista en una variable y se modifica el diccionario, los cambios que hagas en el diccionario se reflejaran en la variable.
dict_val_keys = (diccionario.values() ,  diccionario.keys())   #tendria vista dinamica
diccionario[5] = "Cinq"     # modificamos el diccionario    

print("Vista dinamica almacenando en variable: \n" , dict_val_keys)

# .pop()  = Eliminar una clave y por tanto su valor
diccionario.pop(5)
print("Vista dinamica almacenando en variable(luego de pop) : \n" , dict_val_keys)