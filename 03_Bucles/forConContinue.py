# CONTINUE:
# Esta palabra clave tiene la función de interrumpir la iteración 
# actual de un ciclo y pasar inmediatamente a la siguiente, omitiendo el 
# resto del código dentro del bloque del ciclo para esa iteración particular. 
# Supongamos que tienes una lista de números y quieres imprimir solo los 
# números pares, saltando los números impares: 

numeros = [1,2,3,4,5,6,7,8,9,10]

for numero in numeros:
    if numero % 2 != 0:
        continue
    print(f"Numero: {numero}")

# Este comportamiento resulta útil en situaciones donde se desea saltar 
# una o más iteraciones de un ciclo sin necesidad de terminar por completo 
# la ejecución de este, lo cual puede ser especialmente relevante cuando 
# se trabaja con conjuntos de datos complejos o se necesita aplicar una 
# lógica condicional más sofisticada dentro de los ciclos.