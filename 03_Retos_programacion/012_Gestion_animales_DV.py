
# GESTION DE ANIMALES
baseDatos = []
col1 = "NOMBRE"
col2 = "EDAD"
col3 = "ENFERMO"
col4 = "CEDULA"
ancho = 20

def __validarEdad (num):
    if num <= 0:
        print("Edad incorrecta")

# Agregar animales a la BD
def __agregar(name_x, age_x, sick_x, id_x):

    if age_x >= 0 and sick_x == ("Si" or "No") and id_x >= 0:

        animal = {
            'nombre' : name_x,
            'edad' : age_x,
            'enfermo' : sick_x,
            'cedula_id' : id_x
        }

        baseDatos.append(animal)

        print("\nRegistro exitoso !")
        print(baseDatos)
    
    else:
        if age_x < 0 and sick_x != ("Si" or "No"):
            print("El valor de edad es incorrecto y el estado de salud tambien es erroneo. Intenta de nuevo.")
        elif age_x < 0:
            print("Ha introducido una edad incorrecta. Intente de nuevo.")
        elif sick_x != ("Si" or "No"):
            print("El estado de salud debe ser unicamente SI o NO. Intente de nuevo.")
        elif id_x < 0:
            print("Ingrese un número válido de documento. Intente de nuevo.")



def __buscarPorCedula():
    


# Funcion oara actualizar registro
def __actualizarAnimal(listaNombres, listaEdades, listaEnfermos, listaCedulas_id):
    
    buscar_nombre = input("Nombre del animal a buscar: ")
    




# Funcion para listar toda la base de datos
def __listarAnimales(lista_de_animales):
    print(f'{col1.center(ancho)} | {col2.center(ancho)} | {col3.center(ancho)} | {col4.center(ancho)}')
    for i in lista_de_animales:
        print(f'{str(i['nombre']).center(ancho)} {str(i['edad']).center(ancho)} {str(i['enfermo']).center(ancho)} {str(i['cedula_id']).center(ancho)}')






# Funcion para el menu general
def menu ():
    
    while True:

        print("\n----MENU----")
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
                    name = input("Escribe el nombre del animal:  ").capitalize()

                    age = int(input("Escribe la edad del animal:  ")) 

                    sick = input("El animal está enfermo (Si/No):  ").capitalize()
                    id_cedula = int(input("Ingresa el numero de documento del dueño:  "))

                    __agregar(name, age, sick, id_cedula)
                    
                case "2":
                    __actualizarAnimal()
                case "3":
                    pass
                case "4":
                    __buscarPorCedula(baseDatos)
                case "5":
                    __listarAnimales(baseDatos)
                case "0":
                    pass
                case _:
                    print("Error.")
                    break
        
        except ValueError:
            print("\nOpcion incorrecta. Intenta de nuevo.")

menu()