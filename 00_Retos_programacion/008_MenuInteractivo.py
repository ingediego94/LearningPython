# Menú interactivo simple
# Crea un menú con las opciones:
#     Ingresar rango
    #     Calcular la suma de pares en el rango definido
    #     Calcular la suma de impares en el rango definido
#     Salir
#     Usa while para mostrar el menú hasta que el 
#     usuario elija la opción "Salir".

# Sumar solo numeros pares con FOR
# Sumar solo numeros impares con FOR
# Pide un numero al usuario y usa un ciclo for para sumar todos los números 
# impares entre 1 y ese numero.


#FUNCTIONS
# Function to request 2 numbers
def numbersRequest():
    while True:
        try:
            number_a = int(input("Ingresa el primer número del rango: "))
            number_b = int(input("Ingresa el segunto número del rango: "))
            return number_a, number_b
        except ValueError:
            print("⚠️ Solo se permiten números enteros.\nIntentalo nuevamente.\n")

# Function to odd numbers
def sumOfOddNumbers(num1, num2):
    addition = 0
    for i in range(num1, num2+1):
        if i % 2 != 0:
            addition += i
    return print(f"\n   Resultado:\n    ==> La suma de los impares de {num1} a {num2} es: {addition} \n")


# Function to even numbers
def sumOfEvenNumbers(num1, num2):
    addition = 0
    for i in range(num1, num2+1):
        if i % 2 == 0:
            addition += i
    return print(f"\n   Resultado:\n    ==> La suma de los pares de {num1} a {num2} es: {addition} \n")

# Function to create submenu
def submenu():

    while True:
        print("     Sub-Menú")
        print(" |1| Calcular la suma de los pares del rango.")
        print(" |2| Calcular la suma de los impares del rango")
        print(" |3| Volver al menú anterior.")

        option2 = int(input("\nEscoge tu opcion: \n"))

        if option2 == 1:
            number1, number2 = numbersRequest() 

            sumOfEvenNumbers(number1, number2)


        elif option2 == 2:
            number1, number2 = numbersRequest()

            sumOfOddNumbers(number1, number2)


        elif option2 == 3:
            print("\n↩️ Volviendo al menú principal...\n")
            break
        


# CODE

# Submenu del 1
while True:

    try: 
        
        print("         📖 MENU DE OPCIONES")
        print(" |1| Hacer operaciones.")
        print(" |2| Salir")
    
        option1 = int(input("   \nEscoge tu opcion: \n"))
    
        if option1 == 1:

            submenu()


        elif option1 == 2:
            print("👋 El programa ha finalizado.")
            break
            
        else:
            print("⚠️ Opción inválida. Intenta nuevamente.")

    
    except ValueError:
        print("Has escogido una opción incorrecta. Intentalo nuevamente.")
    
    
