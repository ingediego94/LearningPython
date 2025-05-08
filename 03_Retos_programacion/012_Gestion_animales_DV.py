
# GESTION DE ANIMALES
animales= []
nombre = []
edad = []
enfermo = []

def validarEdad (num):
    pass

def agregar(name_x, age_x, sick_x):
    nombre.append(name_x)
    edad.append(age_x)
    enfermo.append(sick_x)


    animales.append(nombre)
    animales.append(edad)
    animales.append(enfermo)

print(animales)




# Funcion para el menu general
def menu ():
    
    while True:

        print("MENU")
        print("| 1 | Agregar animal.")
        print("| 2 | Actualizar animal.")
        print("| 3 | Eliminar animal.")
        print("| 4 | Listar todos los animales.")
        print("| 0 | Salir.")

        opcion = input("\nIngrese la opcion deseada del menú:\t")

        try:
            match opcion:
                case "1":
                    print(f"\n--- AGREGAR ANIMALES ---")
                    name = input("Escribe el nombre del animal:  ")
                    age = int(input("Escribe la edad del animal:  "))
                    sick = input("El animal está enfermo (Si/No):  ")
                    agregar(name, age, sick)
                    
                case "2":
                    pass
                case "3":
                    pass
                case "4":
                    pass
                case "0":
                    print("\nHas salido del programa, gracias por preferirnos.")
                case _:
                    print("Error.")
                    break
        
        except ValueError:
            print("\nOpcion incorrecta. Intenta de nuevo.")

menu()