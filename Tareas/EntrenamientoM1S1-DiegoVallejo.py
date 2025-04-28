# Crear un sistema de validacion de productos que permita registrar el producto, 
# ingresar su precio unitario, ingresar la cantidad y el descuento.  

# PRESENTADO POR:   DIEGO VALLEJO ZAPATA
# RIWI - MEDELLIN | JORNADA AM |

from datetime import datetime

# Creacion de variables
# PRODUCTO:
print("=" * 45)
print("         REGISTRO DE VENTAS EL RIWI      ")
print("=" * 45)

producto = input("Escriba el nombre del producto: \n\t")

# PRECIO UNITARIO:
precioUn = float(input("Cual es el precio unitario del producto: \n\t"))

while precioUn < 0:
    precioUn = float(input("Ha ingresado un dato incorrecto. \n Por favor ingrese el precio unitario del producto: \n\t"))

# CANTIDAD DE PRODUCTOS:
cantidad = int(input("Ingrese la cantidad de productos adquiridos: \n\t"))

while cantidad < 0:
    cantidad = int(input("Ha ingresado un dato incorrecto. \n Por favor ingrese la cantidad de productos adquiridos: \n\t"))

# DESCUENTO:
descuento = float(input("Ingresa el porcentaje de descuento (%): \n\t"))

while descuento < 0 or descuento > 100:
    descuento = float(input("Ha ingresado un dato incorrecto. \n Ingresa el porcentaje de descuento (solo valores entre 0 y 100): \n\t"))

# Fecha
fechaYHora = datetime.now()


# ELABORACION DE CALCULOS:

# Damos formato al texto del producto comprado
producto = producto.capitalize()

# Damos formato a la fecha y hora para que sea mas legible
formatoFecha = fechaYHora.strftime("%Y-%m-%d")
formatoHora = fechaYHora.strftime("%H:%M:%S")

# precio total sin aplicar descuento 
costoTotalSinDcto = precioUn * cantidad

# Precio aplicando descuento
descuento = descuento / 100
costoConDcto = costoTotalSinDcto * (1-descuento)

# ELABORACION DE LA FACTURA YA FORMATEADA:
print("*" * 45)
print()
print("=" * 45)
print("             ALMACENES RIWI          ")
print("           FACTURA DE COMPRA\n")
print("=" * 45)


print(f"Fecha:\t\t {formatoFecha}")

print(f"Hora:\t\t {formatoHora}")

print("Factura número: 153.001\n")

print("-" * 45)

print("COSTO SIN DESCUENTO")

print("Producto: \t Costo unitario:")

print(f"{producto}:\t\t$ {round(costoTotalSinDcto, 2)}\n")

print("-" * 45)

print(f"COSTO CON DESCUENTO DEL {descuento * 100} %")

print("Producto: \t Costo unitario:")

print(f"{producto}:\t\t${round(costoConDcto,2)}\n")

print(f"Su ahorro fue de:\t${round(costoTotalSinDcto-costoConDcto)}")

print("-" * 45)

print("\n           GRACIAS POR SU COMPRA.\n")

print("               ¡VUELVA PRONTO!")

print("* * * * * * * * * * * * * * * * * * * * * * * ")