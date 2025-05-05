"""
La empresa para la que trabaja, le otorga un premio económico si rebasa $200 de ventas (venta meta) por cliente. La empresa cuenta con un registro en donde están marcadas las ventas de 8 clientes que adquirieron algunos de los productos de la marca. Por cada cliente que rebasó la cantidad meta se 
escribe 1, y si no la rebasa se escribe 2. Si número de clientes que rebasan la venta meta es más de la mitad, se le otorga el premio al promotor. Se requiere de un programa que señale si al promotor se le debe asignar el premio económico
"""
cliente1 = 0
cliente2 = 0
cliente3 = 0
cliente4 = 0

customer = input("Ingrese el número de cliente a registrar: '1-8 \n")

continuar = float(input("Ingresa consumo. Finalizó la operacion? \n '-1'"))
while continuar != -1:
    venta = float(input("Ingrese el valor de la venta"))
