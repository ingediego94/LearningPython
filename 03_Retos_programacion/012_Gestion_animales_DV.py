
# GESTION DE ANIMALES
baseDatos = [
    {'nombre' : 'perro',
    'edad' : 4,
    'enfermo' : 'si',
    'cedula_id' : 1234
    },
    {'nombre' : 'gato',
    'edad' : 5,
    'enfermo' : 'no',
    'cedula_id' : 92922
    },
    {'nombre' : 'elefante',
    'edad' : 85,
    'enfermo' : 'si',
    'cedula_id' : 54545454
    }
]
col1 = "NOMBRE"
col2 = "EDAD"
col3 = "ENFERMO"
col4 = "CEDULA"
ancho = 20

# ARREGLAR ESTA PARTE
# Agregar animales a la BD
def __agregar(name_x, age_x, sick_x, id_x):

    if age_x >= 0 and sick_x in ("si" or "no") and id_x >= 0:

        animal = {
            'nombre' : name_x,
            'edad' : age_x,
            'enfermo' : sick_x,
            'cedula_id' : id_x
        }

        baseDatos.append(animal)

        print("\nRegistro exitoso !")
        print("\n", baseDatos)
    
    else:
        if age_x < 0 and sick_x not in ("si" or "no"):
            print("El valor de edad es incorrecto y el estado de salud tambien es erroneo. Intenta de nuevo.")

        elif age_x < 0:
            print("Ha introducido una edad incorrecta. Intente de nuevo.")

        elif sick_x != 'si' or sick_x != 'no':
            print("El estado de salud debe ser unicamente SI o NO. Intente de nuevo.")

        elif id_x < 0:
            print("Ingrese un número válido de documento. Intente de nuevo.")




def __buscarPorNombre(lista_de_animales):

    buscar_nombre = input('Nombre del animal a buscar:  ').lower()

    for nombre_buscador in lista_de_animales:
        if nombre_buscador["nombre"] == buscar_nombre:
            
            print("\nDatos del animal:")
            print(f"{col1}: {nombre_buscador['nombre']}")
            print(f"{col2}: {nombre_buscador['edad']}")
            print(f"{col3}: {nombre_buscador['enfermo']}")
            print(f"{col4}: {nombre_buscador['cedula_id']}")
            break

    else:
        print("Animal no encontrado en la base de datos.")



def __actualizarAnimal(lista_de_animales):
    buscador = input("Ingresa el nombre del animal a buscar:  ").lower()

    for nombreAnimal in lista_de_animales:
        if nombreAnimal['nombre'] == buscador:
            nuevaEdad = int(input('Nueva edad:  '))
            nuevoEnfermo = input("Nuevo estado enfermedad:  ").lower()

            nombreAnimal['enfermo'] = nuevoEnfermo
            nombreAnimal['edad'] = nuevaEdad

            print(f'Registro de {buscador} actualizado exitosamente.')
            break
    else:
        print(f'{buscador} no se encuentra en la base de datos.')


# Funcion para listar toda la base de datos
def __listarAnimales(lista_de_animales):
    print(f'{col1.center(ancho)} | {col2.center(ancho)} | {col3.center(ancho)} | {col4.center(ancho)}')
    
    for i in lista_de_animales:
        print(f'{str(i['nombre']).center(ancho)} {str(i['edad']).center(ancho)} {str(i['enfermo']).center(ancho)} {str(i['cedula_id']).center(ancho)}')



def __eliminarAnimales(lista_de_animales):
    buscarAnimal = input("Nombre del animal a eliminar: ").lower()

    for buscador in lista_de_animales:
        if buscador['nombre'] == buscarAnimal:
            confirmacion = input(f"Confirma que desea borrar el registro de {buscarAnimal} ?  ").lower()
            if confirmacion == 'si':
                lista_de_animales.remove(buscador)
                print(f"{buscarAnimal} se ha eliminado con exito.")
            break
    else:
        print(f"{buscarAnimal} no se ha encontrado en la base de datos.")


def __salirSistema():
    salir = input("Desea salir del sistema? Si / No  ").lower()

    if salir == "si":
        print("Saliendo del sistema")
        return True
    
    elif salir == "no":
        print("Regresando al menu. ")
        return False

    else:
        print("opcion erronea.")
        return False





# Funcion para el menu general
def menu ():
    
    while True:

        print("\n----MENU----")
        print("| 1 | Agregar animal.")
        print("| 2 | Actualizar animal.")
        print("| 3 | Eliminar animal.")
        print("| 4 | Buscar por nombre.")
        print("| 5 | Listar todos los animales.")
        print("| 0 | Salir.")

        opcion = input("\nIngrese la opcion deseada del menú:\t")

        try:
            match opcion:
                case "1":       # | 1 | Agregar animal.

                    print(f"\n--- AGREGAR ANIMALES ---")
                    name = input("Escribe el nombre del animal:  ").lower()

                    age = int(input("Escribe la edad del animal:  ")) 

                    sick = input("El animal está enfermo (Si/No):  ")
                    sick = sick.strip().lower()

                    id_cedula = int(input("Ingresa el numero de documento del dueño:  "))

                    __agregar(name, age, sick, id_cedula)
                    
                case "2":       # | 2 | Actualizar animal.
                    __actualizarAnimal(baseDatos)

                case "3":       # | 3 | Eliminar animal.
                    __eliminarAnimales(baseDatos)

                case "4":       # | 4 | Buscar por nombre.
                    __buscarPorNombre(baseDatos)

                case "5":       # | 5 | Listar todos los animales
                    __listarAnimales(baseDatos)

                case "0":       # | 0 | Salir.
                    if __salirSistema():
                        break

                case _:
                    print("Error.")
                    
        
        except ValueError:
            print("\nOpcion incorrecta. Intenta de nuevo.")

menu()



