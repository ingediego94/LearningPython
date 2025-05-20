# medicion de rendimiento lista vs tupla. La tupla es mucho mas rapida

import timeit

lista = ['lista', 'pera', 'cali','carlos',123, 4.555555, 565, True, False]

tulpa = ('lista', 'pera', 'cali','carlos',123, 4.555555, 565, True, False)

tiempoLista = timeit.timeit(stmt='["lista", "pera", "cali","carlos",123, 4.555555, 565, True, False]', number=10000000)
tiempoTupla = timeit.timeit(stmt='("lista", "pera", "cali","carlos",123, 4.555555, 565, True, False)', number=10000000)

tiempoNeto = tiempoLista - tiempoTupla

print(tiempoNeto)
