# ENTRENAMIENTO SEMANA 2, PYTHON.
# Presentado por: Diego Vallejo Z. 
# Riwi - Clan Hopper

# Importamos libreria
from datetime import datetime


# funcion para validar lista
def validate_List(lista):
    return all(isinstance(i, float) and 0 <= i <= 100 for i in lista)

# Variables para alojar datos de fecha y hora.
dateAndTime = datetime.now()
dateFormated = dateAndTime.strftime("%Y-%m-%d")
hourFormated = dateAndTime.strftime("%H:%M:%S")

# Creacion lista de notas
gradesList = []

# creacion de lista de subjects
subjects = [
    "Fisica",
    "Ética",
    "Cálculo",
    "Química"
    ]

minimumGrade = 70.0

RED = '\033[31m'
GREEN = '\033[32m'
RESET = '\033[0m' 
BLUE = '\033[34m'
YELLOW = '\033[33m'

# Impresión de mensajes por pantalla
print("=" * 53)

print(f"{BLUE}||         SISTEMA DE CALIFICACIONES RIWI          ||{RESET}")

print("=" * 53)


studentName = input("Nombre del estudiante: ").title()

c = print(f"\nHola {studentName}, bienvenido al sistema de \ncalificaciones de Riwi.")

print("." * 53)

print(f"Ingresa tu calificacion (0-100 separada por comas).\n")

# Pedimos el listado de calificaciones con un while true y luego con un try except para capturar excepciones
while True:

    gradesToConvert = input(f"Escribe tus calificaciones en el siguiente orden: \n{subjects}\n")

    try:
        # Almacenamos los valores como elementos independientes en la lista
        gradesInText = [nota.strip() for nota in gradesToConvert.split(',')]

        gradesList = [round(float(nota),1) for nota in gradesInText] 
        
        for num in range(0, len(gradesList)):
            
            if gradesList[num] < 0 or gradesList[num] > 100:
                print(f"Ha ingresado el número {gradesList[num]}, el cual está fuera del \nrango de 0 a 100.\n")

        break
        

    except ValueError:
        print("\n⚠️  Error: No has ingresado un caracter válido. Intenta nuevamente.\n")



listValidation = validate_List(gradesList)

if listValidation == True:

    if listValidation == True and (len(gradesList) == len(subjects)):

        print(f"\nLas calificaciones son: {gradesList}")


        print('=' * 53)
        print('           REPORTE FINAL DE CALIFICACIONES           ')
        print('-' * 53)
        print(f"Fecha:{'\t'*5} {dateFormated}")

        print(f"Hora:{'\t'*5} {hourFormated}")
        print(f"Nombre del estudiante: \t\t\t{studentName}")
        print('-' * 53)

        # Validamos si el estudiante aprobo o reprobo
        for i in range(0, len(subjects)):
            if gradesList[i] >= minimumGrade:
                print(f"\t✅ {GREEN}Aprobaste {subjects[i]} con: \t{gradesList[i]}{RESET}")
            else:
                print(f"\t⛔ {RED}Reprobaste {subjects[i]} con: \t{gradesList[i]}{RESET}")

        print('=' * 53)
        print(f'{BLUE}              PROMEDIO DE CALIFICACIONES              {RESET}')
        print('-' * 53)

        # Obtenemos el promedio de las notas con un for y lo mostramos por pantalla
        sumOfGrades = 0

        for i in range(0, len(gradesList)):
            sumOfGrades += gradesList[i]

        averageOfGrades = sumOfGrades / len(gradesList)

        print(f"\t\tTu promedio de notas es: {round(averageOfGrades, 1)}")

        print("=" * 53)
        print(f'{BLUE}            COMPARATIVO DE CALIFICACIONES            {RESET}')
        print('-' * 53)
        # Notas basadas en un valor especifico
        compareGrades = input("¿Deseas comparar tus notas con un valor específico? \n SI - NO\n")

        compareGrades = compareGrades.upper()

    # Desea comparar notas?
        match compareGrades:
            # SI desea comparar notas
            case 'SI': 
                
                while True:
                    try:

                        #Comparar notas
                        valueGradeToCompare = float(input("Ingresa la nota a comparar:  "))
                        if not 0 <= valueGradeToCompare <= 100:
                            raise ValueError("El número está fuera del rango permitido.")
                        break
                        
                    except ValueError as e:
                        
                        print("\n⚠️  Error:", e)
                        print("Solo se permiten números entre 0 y 100. \nIntenta nuevamente.\n")

                counter = 0
                iterator = 0

                # while para contar cuántas calificaciones son mayores que el valor especificado
                while iterator != len(gradesList):

                    if gradesList[iterator] > valueGradeToCompare:
                        counter += 1
                    iterator += 1

                # Imprime por pantalla cuantas notas son iguales a valueGradeToCompare 
                
                if counter > 0:
                    print(f"Tienes {counter} calificacion(es) mayor(es) a {valueGradeToCompare}")
                elif counter == 0:
                    print(f"Tienes {counter} calificaciones mayores a {valueGradeToCompare}")
                
                # for para verificar la presencia de una calificación específica y contar cuántas veces aparece
                gradesRepeatCounter = 0
                for grade_list in gradesList:
                    if valueGradeToCompare == grade_list:
                        gradesRepeatCounter += 1

                
                if gradesRepeatCounter != 0:
                    print(f"La nota {valueGradeToCompare} aparece {gradesRepeatCounter} veces. ")
                else:
                    print(f"La nota {valueGradeToCompare} aparce {gradesRepeatCounter} veces.")

                print(f"\n\t{YELLOW}  {studentName.upper()}, GRACIAS POR PREFERIRNOS {RESET}")
                print("=" * 53)
                
            
            # NO desea comparar notas
            case 'NO':
                print("Deseaste no comparar tus notas.")
            
            # Opcion INCORRECTA para comparar notas
            case _:
                print(f"Has seleccionado una opcion incorrecta. \nSolo se adminte SI o NO.")

    else:
        print("-" * 53)
        print("La cantidad de notas ingresadas no concuerda con la \ncantidad de materias. Por favor revisa e intenta\nnuevamente.")
        print("=" * 53)


else:
    print("Intenta nuevamente. ")