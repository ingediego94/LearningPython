"""
Crear un diccionario para almacenar información sobre estudiantes y realizar algunas operaciones 
básicas como agregar, modificar y mostrar datos.

Instrucciones:
1. Crea un diccionario llamado estudiantes, donde las claves sean los nombres de los estudiantes y 
los valores sean otro diccionario con las claves edad y calificacion.

2. El programa debe permitir al usuario realizar las siguientes operaciones:
    Agregar un nuevo estudiante (nombre, edad, calificación).
    Modificar la calificación de un estudiante.
    Mostrar la información de todos los estudiantes.
    Eliminar un estudiante por su nombre.
"""

estudiantes = {
    'Diego' : {'edad' : 23, 'calificacion' : 5},
    'Carlos' : {'edad' : 20, 'calificacion' : 4},
    'Maria' : {'edad' : 13, 'calificacion' : 5}
}

#  1. Agregar estudiantes
def agregarEstudiante(name, age, grade):
    estudiantes[name] = {
        'edad' :  age,
        'calificacion' : grade
    }

    print("Registro exitoso. ")


# 2. Modificar nota del estudiante
def modificarCalificacion(nombrex, calificacionx, listaEstudiantes):
    if nombrex in listaEstudiantes:
        listaEstudiantes[nombrex]['calificacion'] = calificacionx
        print(f"Se modificó la calificacion de {nombrex} a {calificacionx}")
    else:
        print(f"El estudiante {nombrex} no se encuentra en el listado de estudiantes.")


# 3. Mostrar toda la informacion
def mostrarInformacion(listaEstudiantes):

    print("NOMBRE       EDAD        CALIFICACION")
    for nombre, info in listaEstudiantes.items():
        print(f" {nombre:<12}  {info['edad']:<10}  {info['calificacion'] } ")

    """
    info['edad']: accede al valor asociado con la clave 'edad' en el diccionario info.
    :<10: es un formato de alineación que indica:
        : comienza la especificación del formato.
        < significa que el valor debe estar alineado a la izquierda.
        10 indica que debe ocupar un ancho total de 10 caracteres.
    """


# 4. Eliminar estudiante
def eliminarEstudiante(name, listaEstudiantes):
    if name in listaEstudiantes:
        del listaEstudiantes[name]
        print(f"Se ha eliminado al estudiante {name}")
    else:
        print(f"El nombre {name} no se encuentra en el listado de estudiantes.")



def menu():
            
    while True:
        try:        
            print('\n-- MENU --')
            print("1  Agregar un nuevo estudiante. ")
            print("2  Modificar una calificacion. ")
            print("3  Mostrar la informacion de todos los estudiantes. ")
            print("4  Eliminar un estudiante por su nombre. ")

            opcion = int(input("\nIngrese la opcion que desea realizar:  ").strip())

            if 1 <= opcion <= 4:
                
                # Agregar estudiante
                if opcion == 1:
                    nombreEstudiante = input("Ingresa el nombre del estudiante:  ").strip().capitalize()
                    edadEstudiante = int(input("Cual es la edad del estudiante:  ").strip())
                    notaEstudiante = int(input("Cual es la nota del estudiante: ").strip())

                    agregarEstudiante(nombreEstudiante, edadEstudiante, notaEstudiante)


                # Modificar nota del estudiante
                elif opcion == 2:
                    nom_estud = input("Ingresa el nombre del estudiante a modificar la nota: ").strip().capitalize()
                    notaModificada = int(input("Ingresa la nueva calificacion: "))
                    modificarCalificacion(nom_estud, notaModificada, estudiantes)


                # Mostrar todo el listado de estudiantes
                elif opcion == 3:
                    mostrarInformacion(estudiantes)
                    

                # Eliminar estudiante
                elif opcion == 4:
                    student_name = input("Escriba el nombre del estudiante a eliminar: ").strip().capitalize()

                    eliminarEstudiante(student_name, estudiantes)
                    

                else:
                    print("Opcion incorrecta.")

            else:
                print("Ha escogido una opcion incorrecta.")
        
        except ValueError:
            print("Opcion erronea.")


menu()