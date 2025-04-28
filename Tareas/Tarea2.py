# El programa que vas a desarrollar en este entrenamiento debe:
#   Determinar el estado de aprobación:
#   Solicitar al usuario ingresar una calificación numérica (de 0 a 100)
#   Evaluar si el estudiante ha aprobado o reprobado basándose en la calificación ingresada
#   Calcular el promedio:
#   Permitir al usuario ingresar una lista de calificaciones (separadas por comas)
#   Calcular y mostrar el promedio de las calificaciones en la lista
#   Contar calificaciones mayores:
#   Preguntar al usuario por un valor específico
#   Contar cuántas calificaciones en la lista son mayores que este valor
#   Verificar y contar calificaciones específicas:
#   Permitir al usuario ingresar una lista de calificaciones (separadas por comas)
#   Calcular y mostrar el promedio de las calificaciones en la lista

# Implementación de la Solución:
#   Entrada de datos:
#   Solicita al usuario ingresar una calificación numérica y valida la entrada
#   Permite al usuario ingresar una lista de calificaciones y un valor específico para comparar
#   Condicionales:
#   Utiliza if, if-else e if-elif-else para determinar el estado de aprobación y mostrar mensajes adecuados
#   Cálculo del promedio:
#   Implementa un ciclo for para recorrer la lista de calificaciones y calcular el promedio
#   Conteo de calificaciones mayores:
#   Usa un ciclo while para contar cuántas calificaciones son mayores que el valor especificado
#   Verificación y conteo:
#   Emplea un ciclo for para verificar la presencia de una calificación específica y contar cuántas veces aparece, 
#   utilizando break y continue para controlar el flujo


calificacion = int(input("Ingresa tu calificacion (0-100 separada por comas): "))

listaNotas = []

minimaAprobatoria = 70

if calificacion >= 70:
    print("Aprobaste")
else:
    print("Reprobado")