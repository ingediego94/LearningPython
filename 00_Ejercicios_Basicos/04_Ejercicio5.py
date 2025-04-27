# Una tienda ofrece un dcto del 15% sobre el total de la compra y un cliente desea saber cuanto deberá pagar finalmente por su compra.

descuento = 0.15

articulo1 = float(input("Precio articulo 1: "))
articulo2 = float(input("Precio articulo 2: "))
articulo3 = float(input("Precio articulo 3: "))
articulo4 = float(input("Precio articulo 4: "))

subtotal = articulo1 + articulo2 + articulo3 + articulo4

total = subtotal * (1-descuento)

totDescuento = subtotal - total

print(f"El total a pagar luego del descuento del {descuento*100}% es de: ${total}. \n Su descuento fue de: ${totDescuento:.2f}")