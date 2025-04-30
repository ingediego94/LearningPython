# ENTRENAMIENTO SEMANA 2, PYTHON.
# Presentado por: Diego Vallejo Z. 
# Riwi - Clan Hopper

# Importamos libreria
from datetime import datetime


# funcion para validar lista
def validar_lista(lista):
    return all(isinstance(i, float) and 0 <= i <= 100 for i in lista)

# Variables para alojar datos de fecha y hora.
fechaYHora = datetime.now()
formatoFecha = fechaYHora.strftime("%Y-%m-%d")
formatoHora = fechaYHora.strftime("%H:%M:%S")

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


nombre = input("Nombre del estudiante: ").title()

bienvenida = print(f"\nHola {nombre}, bienvenido al sistema de \ncalificaciones, de Riwi.")

print("." * 53)

print(f"Ingresa tu calificacion (0-100 separada por comas).\n")

# Pedimos el listado de calificaciones con un while true y luego con un try except para capturar excepciones
while True:

    calificaciones = input(f"Escribe tus calificaciones en el siguiente orden: \n{materias}\n")

    try:
        # Almacenamos los valores como elementos independientes en la lista
        calificacionesEnTexto = [nota.strip() for nota in calificaciones.split(',')]

        listaNotas = [round(float(nota),1) for nota in calificacionesEnTexto] 
        
        for num in range(0, len(listaNotas)):
            
            if listaNotas[num] < 0 or listaNotas[num] > 100:
                print(f"Ha ingresado el número {listaNotas[num]}, el cual está fuera del \nrango de 0 a 100.\n")

        break
        

    except ValueError:
        print("\n⚠️  Error: No has ingresado un caracter válido. Intenta nuevamente.\n")



validacionLista = validar_lista(listaNotas)

if validacionLista == True:

    if validacionLista == True and (len(listaNotas) == len(materias)):

        print(f"\nLas calificaciones son: {listaNotas}")


        print('=' * 53)
        print('           REPORTE FINAL DE CALIFICACIONES           ')
        print('-' * 53)
        print(f"Fecha:{'\t'*5} {formatoFecha}")

        print(f"Hora:{'\t'*5} {formatoHora}")
        print('-' * 53)

        # Validamos si el estudiante aprobo o reprobo
        for i in range(0, len(materias)):
            if listaNotas[i] >= minimaAprobatoria:
                print(f"\t✅ Aprobaste {materias[i]} con: \t{listaNotas[i]}")
            else:
                print(f"\t⛔ Reprobaste {materias[i]} con: \t{listaNotas[i]}")

        print('=' * 53)
        print('              PROMEDIO DE CALIFICACIONES              ')
        print('-' * 53)

        # Obtenemos el promedio de las notas con un for y lo mostramos por pantalla
        sumatoriaNotas = 0

        for i in range(0, len(listaNotas)):
            sumatoriaNotas += listaNotas[i]

        promedioNotas = sumatoriaNotas / len(listaNotas)

        print(f"\t\tTu promedio de notas es: {round(promedioNotas, 1)}")

        print("=" * 53)
        print('            COMPARATIVO DE CALIFICACIONES            ')
        print('-' * 53)
        # Notas basadas en un valor especifico
        compararNotas = input("¿Deseas comparar tus notas con un valor específico? \n SI - NO\n")

        compararNotas = compararNotas.upper()

    # Desea comparar notas?
        match compararNotas:
            # SI desea comparar notas
            case 'SI': 
                
                while True:
                    try:

                        #VALIDAR ESTA PARTE
                        valorNotaComparar = float(input("Ingresa la nota a comparar:  "))
                        if not 0 <= valorNotaComparar <= 100:
                            raise ValueError("El número está fuera del rango permitido.")
                        break
                        
                    except ValueError as e:
                        #print("\n⚠️  Error: No has ingresado un caracter válido o este se encuentra por fuera del rango permitido (0-100). \nIntenta nuevamente.\n")
                        print("\n⚠️  Error:", e)
                        print("Solo se permiten números entre 0 y 100. \nIntenta nuevamente.\n")

                contador = 0
                iterador = 0

                # while para contar cuántas calificaciones son mayores que el valor especificado
                while iterador != len(listaNotas):
                #for i in range(0, len(listaNotas)):
                    if listaNotas[iterador] > valorNotaComparar:
                        contador += 1
                    iterador += 1

                #VALIDAR---
                if contador == 1:
                    print(f"Tienes {contador} calificacion igual a {valorNotaComparar}")
                elif contador > 1:
                    print(f"Tienes {contador} calificaciones mayores a {valorNotaComparar}")

                
                # for para verificar la presencia de una calificación específica y contar cuántas veces aparece
                contadorRepeticionNota = 0
                for lista_nota in listaNotas:
                    if valorNotaComparar == lista_nota:
                        contadorRepeticionNota += 1
                    #else:
                        #print(f"La nota {valorNotaComparar} aparce {contadorRepeticionNota} veces.")
                
                if contadorRepeticionNota != 0:
                    print(f"La nota {valorNotaComparar} aparece {contadorRepeticionNota} veces. ")
                else:
                    print(f"La nota {valorNotaComparar} aparce {contadorRepeticionNota} veces.")

                print(f"\n\t  {nombre.upper()}, GRACIAS POR PREFERIRNOS ")
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