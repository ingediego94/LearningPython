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


# Presentado por: Diego Vallejo Z. 
# Riwi - Clan Hopper

# Creacion lista de notas
listaNotas = []

# creacion de lista de materias
materias = [
    "Fisica",
    "Ética",
    "Cálculo",
    "Química"
    ]

minimaAprobatoria = 70.0

# Impresión de mensajes por pantalla
print("=" * 53)

print("||         SISTEMA DE CALIFICACIONES RIWI          ||")

print("=" * 53)


print(f"Ingresa tu calificacion (0-100 separada por comas).\n")

calificaciones = input(f"Escibe tus calificaciones en el siguiente orden: \n{materias}\n")


# Almacenamos los valores como elementos independientes en la lista
calificacionesEnTexto = [nota.strip() for nota in calificaciones.split(',')]

listaNotas = [round(float(nota),1) for nota in calificacionesEnTexto]

print(f"Las calificaciones son: {listaNotas}")


print('=' * 53)
print('           REPORTE FINAL DE CALIFICACIONES           ')
print('-' * 53)

# Validamos si el estudiante aprobo o reprobo
for i in range(0, len(materias)):
    if listaNotas[i] >= minimaAprobatoria:
        print(f"\t✅ Aprobaste {materias[i]} con: \t{listaNotas[i]}")
    else:
        print(f"\t⚠️  Reprobaste {materias[i]} con: \t{listaNotas[i]}")

print('=' * 53)
print('              PROMEDIO DE CALIFICACIONES              ')
print('-' * 53)

# Obtenemos el promedio de las notas con un for y lo mostramos por pantalla
sumatoriaNotas = 0

for i in range(0, len(listaNotas)):
    sumatoriaNotas += listaNotas[i]

promedioNotas = sumatoriaNotas / len(listaNotas)

print(f"\t\tTu promedio de notas es: {round(promedioNotas, 2)}")

print("=" * 53)
print('            COMPARATIVO DE CALIFICACIONES            ')
print('-' * 53)
# Notas basadas en un valor especifico
compararNotas = input("¿Deseas comparar tus notas con un valor específico? \n SI - NO\n")

compararNotas = compararNotas.upper()

match compararNotas:
    case 'SI': 
        valorNotaComparar = float(input("Ingresa la nota comparativa: "))

        contador = 0
        iterador = 0

        # while para contar cuántas calificaciones son mayores que el valor especificado
        while iterador != len(listaNotas):
        #for i in range(0, len(listaNotas)):
            if listaNotas[iterador] > valorNotaComparar:
                contador += 1
            iterador += 1
        print(f"Tienes {contador} calificaciones mayores a {valorNotaComparar}")

# ARREGLAR ESTA PARTE 
        # for para verificar la presencia de una calificación específica y contar cuántas veces aparece
        #valorNotaComparar = 0

        for lista_nota in listaNotas:
            if valorNotaComparar == lista_nota:
                contadorRepecionNota += 1
                print(f"La nota '{lista_nota}' aparece {contadorRepecionNota} veces. ")
            else:
                print(f"La nota {valorNotaComparar} aparce {valorNotaComparar} veces.")
        
    case 'NO':
        print("Deseaste no comparar tus notas.")
    case _:
        print(f"Has seleccionado una opcion incorrecta. \nSolo se adminte SI o NO.")