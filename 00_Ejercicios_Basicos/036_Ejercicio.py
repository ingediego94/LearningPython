# Usa un bucle for, randrange y una expresión condicional para simular 20 tiros de moneda, mosrando A para águila y S para Sello

import random as rd

for i in range(20):
    print("A" if rd.randrange(2) == 0 else "S", end=', ')

