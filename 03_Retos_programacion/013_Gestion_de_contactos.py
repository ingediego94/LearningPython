"""
Crear un diccionario para gestionar los contactos, donde la clave sea el nombre del contacto 
y el valor sea su número de teléfono. El programa permitirá agregar nuevos contactos.
Crea un diccionario llamado contactos donde cada clave sea el nombre de un contacto y su valor 
sea el número de teléfono.

El programa debe permitir al usuario realizar las siguientes operaciones:

    1. Agregar un nuevo contacto (nombre, número de teléfono).
    2. Mostrar todos los contactos almacenados.
    3. Buscar un contacto por su nombre.
"""

contactos = {
    'Diego' : 3133224545,
    'Camila' : 3004665332
}

def __agregarContacto(name, telephone):
    contactos[name] = telephone

    print("Registro exitoso !")
    print(f'{name} con número {telephone} se agregado exitosamente a la agenda.')


def __mostrarContactos(listaContactos):

    print('Nombre    Telefono')
    
    for contactox, telefonox in listaContactos.items():
        print(f"{contactox} : {telefonox}")
    print('\nFin de contactos.')
    

def __buscarPorNombre(namex, listaContactos):

    for nombreContacto, telefonox1 in listaContactos.items():
        if nombreContacto == namex:
            print("Nombre       Teléfono")
            print(f'{nombreContacto} : {telefonox1}')
            break
    else:
        print('Contacto no encontrado en la agenda.')


def __eliminarContacto(buscax, listaContactos):

    for name in listaContactos:
        if buscax == name:
            listaContactos.pop(buscax)
            print("Contacto eliminado con exito.")
            break
    else:
        print("Contacto no encontrado en la agenda.")


def __salir(z):
    if z == 'si':
        print("Saliendo del sistema.")
        return True
    
    elif z == 'no':
        print('Regresando al menu.')
        return False
    
    else:
        print("Opcion erronea.")
        return False

def __menu():

    while True:

        try:
            print('\n -- MENU CONTACTOS --')

            opcion = input("""
            | 1 | Agregar nuevo contacto.
            | 2 | Mostrar todos los contactos.
            | 3 | Buscar por el nombre.
            | 4 | Eliminar contacto.
            | 0 | Salir.
            
            Escribe el número de la opcion deseada:  
            """)
            if opcion == '1':
                nombre = input('Nombre del nuevo contacto: ').capitalize().strip()
                telefono = int(input('Numero de telefono: ').strip())

                __agregarContacto(nombre, telefono)
                
            elif opcion == '2':
                __mostrarContactos(contactos)
                
            elif opcion == '3':
                buscador = input('Nombre del contacto a buscar: ').capitalize().strip()
                __buscarPorNombre(buscador, contactos)
                
            elif opcion == '4':
                buscador = input('Nombre del contacto a buscar: ').capitalize().strip()
                __eliminarContacto(buscador, contactos)
                
            elif opcion == '0':
                salida = input("Desea salir del sistema?").lower().strip()
                if __salir(salida):
                    break
                
            else:
                print('Ha seleccionado una opcion incorrecta. Intenta de nuevo')

        except ValueError:
            print('Error grave')

__menu()