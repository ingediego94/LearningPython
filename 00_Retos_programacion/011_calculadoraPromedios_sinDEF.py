# Crea un programa en Python que permita calcular el promedio de notas de varios estudiantes. 
# El programa debe cumplir con los siguientes requisitos:
#     Debe solicitar al usuario cuántos estudiantes va a ingresar.
#     Por cada estudiante, debe:
#         Pedir su nombre.
#         Pedir tres notas (de 0 a 5).
#     Debes usar funciones para:
#         Solicitar los datos de un estudiante.
#         Calcular el promedio de las tres notas.
#         Mostrar si el estudiante aprueba (promedio ≥ 3.0) o reprueba.



numberOfStudents = int(input("De cuantos estudiantes deseas ingresar las notas?  "))

studentsCounter = 0

final_grades = {}

while studentsCounter < numberOfStudents:

    studentName = input("Nombre del estudiante: ")
    gradesToConvert = input("Ingresa las notas separadas por comas: ")
    
    try:
        gradesInText = [gradex for gradex in gradesToConvert.split(',')]

        gradesList = [round(float(grade), 1) for grade in gradesInText]

        for num in range(0 , len(gradesList)):
            if gradesList[num] < 0 or gradesList[num] > 5:
                print(f"Ha ingresado el número {gradesList[num]}, el cual está fuera del rango de 0 a 100.")
        
        final_grades[studentName] = gradesList
        
        print(final_grades)


        # contador de estudiantes
        studentsCounter += 1

    except ValueError:
        print("Error: has ingresado un caracter inválido. Intenta nuevamente.")

averages = {}

for clave, valores in final_grades.items():
    average = round(sum(valores) / len(valores), 1)
    averages[clave] = average

print(averages)