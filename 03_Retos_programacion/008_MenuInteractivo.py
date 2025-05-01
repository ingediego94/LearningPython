# Menú interactivo simple
# Crea un menú con las opciones:
#     Ingresar rango
#     Calcular la suma de pares en el rango definido
#     Calcular la suma de impares en el rango definido
#     Salir
#     Usa while para mostrar el menú hasta que el 
#     usuario elija la opción "Salir".

# Sumar solo numeros impares con FOR
# Pide un numero al usuario y usa un ciclo for para sumar todos los números 
# impares entre 1 y ese numero.


# Function to odd numbers
def sumOfOddNumbers(num1, num2):
    addition = 0
    for i in range(num1, num2+1):
        if i % 2 != 0:
            addition += i
    return print(f"La suma de los impares de {num1} a {num2} es: {addition} ")


# Function to even numbers
def sumOfEvenNumbers(num1, num2):
    addition = 0
    for i in range(num1, num2+1):
        if i % 2 == 0:
            addition += i
    return print(f"La suma de los pares de {num1} a {num2} es: {addition} ")





# Submenu del 1



try: 
    
    print("MENU DE OPCIONES")
    print("|1| Ingresar el rango de números.")
    print("|2| Salir")
    
    option = input("Escoge tu opcion: ")
    
    if option == 1:
        print("Sub-Menú")
        print("|1| Calcular la suma de los pares del rango.")
        print("|2| Calcular la suma de los impares del rango")
        print("|3| Volver a mostrar el menú")
        
    elif option == 2:
        print("El programa ha finalizado.")
        #break
        
    else:
        print("Error.")

    
except ValueError:
    print("Has escogido una opción incorrecta. Intentalo nuevamente.")
    
    

# Pedimos los datos al usuario.
print("Ingresa el rango desde cual número deseas hacer la suma de los impares.")

number1 = int(input("Escribe el número inicial: "))

number2 = int(input("Escribe el número final: "))

# Aplicamos la funcion y obtenemos el resultado
output = sumOfOddNumbers(number1, number2)