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

    for nombreContacto in listaContactos:
        if nombreContacto == namex:
            print("Encontrado.")



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
                buscador = input('Nombre del contacto a buscar: ').capitalize()
                __buscarPorNombre(buscador, contactos)
                
            elif opcion == '4':
                #__eliminarContacto()
                pass
            elif opcion == '0':
                #__salir()
                pass
            else:
                print('Ha seleccionado una opcion incorrecta. Intenta de nuevo')

        except ValueError:
            print('Error grave')

__menu()