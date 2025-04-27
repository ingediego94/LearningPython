# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.

pesoPayaso = 112

pesoMuneca = 75

cantPayasos = int(input("Cual es la cantidad de payasos:\n"))
cantMunecas = int(input("Cual es la cantidad de muñecas:\n"))

pesoTotPayasos = pesoPayaso * cantPayasos

pesoTotMunecas = pesoMuneca * cantMunecas

pesoTotal = (pesoTotPayasos + pesoTotMunecas) / 1000



print(f"El peso total de las muñecas es de: {pesoTotMunecas/1000} Kg.")
print(f"El peso total de los payasos es de: {pesoTotPayasos/1000} Kg.")
print(f"El peso total del paquete a enviar es de: {pesoTotal} Kg.")