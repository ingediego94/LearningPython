# Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.

precio = input("Cual es el precio del producto con dos decimales? ")

print("El precio es: " + precio[:precio.find('.')] + " euros con " + precio[precio.find('.')+1:] + " centimos")