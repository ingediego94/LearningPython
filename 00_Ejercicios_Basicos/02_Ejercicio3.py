# Hacer un programa para intercambiar el valor de 2 variables

# a= 10     a=10
# b=5       b=5

a = int(input("Ingrese un numero: "))
b = int(input("Ingrese otro numero: "))

a , b = b , a       # Aqui cambiarn los valores

print(f"El nuevo valor de a es: {a}")
print(f"El nuevo valor de b es: {b}")