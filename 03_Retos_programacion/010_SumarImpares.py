# Sumar solo numeros impares con FOR
# Pide un numero al usuario y usa un ciclo for para sumar todos los números 
# impares entre 1 y ese numero.


# Creacion de la funcion
def sumOfImpairs(num1, num2):
    addition = 0
    for i in range(num1, num2+1):
        if i % 2 != 0:
            addition += i
    return print(f"La suma de los impares de {num1} a {num2} es: {addition} ")

# Pedimos los datos al usuario.
print("Ingresa el rango desde cual número deseas hacer la suma de los impares.")

number1 = int(input("Escribe el número inicial: "))

number2 = int(input("Escribe el número final: "))

# Aplicamos la funcion y obtenemos el resultado
output = sumOfImpairs(number1, number2)
