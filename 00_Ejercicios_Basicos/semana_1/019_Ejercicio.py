# Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.

precioPan = 3.49

descuento = 0.60

panNoDia = int(input("Cuantas barras vendidas no son del dia? \n"))

total = (1 - descuento) * precioPan * panNoDia

print("El precio habitual de una barra de pan es de: {}".format(precioPan))

print("El descuento por no ser un pan del día es de: {}%".format(descuento*100))

print("El total a pagar es de: {}".format(round(total,2)))

