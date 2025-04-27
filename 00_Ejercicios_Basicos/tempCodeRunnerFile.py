import numpy as np

# Array con la funcion 'ARRAY([])'
a = np.array([1,2,3,4,5])
print(f"array 'a' es: {a} \n")

# Array con la funcion 'ARANGE()' (num inicial, num a alcanzar -1, salto)
b = np.arange(1, 14, 2)
print(f"arange 'b' es: {b} \n")

# Array 'ARANGE' de 1 a 10 con salto de 0.5
c = np.arange(1, 11, 0.5)
print(f"arange 'c' es: {c} \n")

# Array con 'LINSPACE()'  (num inicial, num final, cuantos num medios quiero)
d = np.linspace(1, 8, 5)
print(f"linspace 'd' es: {d} \n")

# Array aleatorio con 'RANDOM.RANDOM([])' de dimensiones 3 * 2
e = np.random.random([3, 2])
print(f"random 'e' es: {e} \n")

# que tipo de dato es una array y un arange
print(f"El tipo de dato de 'a' es: {type(a)}")
print(f"El tipo de dato de 'b' es: {type(b)}")
print(f"El tipo de dato de 'c' es: {type(c)}")
print(f"El tipo de dato de 'd' es: {type(d)}")
print(f"El tipo de dato de 'e' es: {type(e)}\n ")

# Conocer la dimension:  e.ndim
print(f"La dimension de 'e' es: {e.ndim}")

# Conocer la forma:  e.shape
print(f"La forma de 'e' es: {e.shape}")

# Conocer el tamaño:  e.size
print(f"El tamaño de 'e' es: {e.size}")

# Conocer el tipo de dato:  e.dtype
print(f"El tipo de dato de 'e' es: {e.dtype}")