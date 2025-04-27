# Juego del gran 8
# crea un programa que lnce dos dados de tal manera que al sumarlos si da 8 gana, si da 7 pierde, y si sale cualquier otro numero sigue jugando hasta ganar o perder. Debe mostrar la suma de los dados en cada intento.

import random

def lanzar ():
    d1 = random.randrange(1, 7)
    d2 = random.randrange(1, 7)
    return(d1, d2)

def mostrarlos(dades):
    d1, d2 = dades
    print(f"La suma de los dados {d1} + {d2} = {sum(dades)}")

valoresConseguidos = lanzar ()
mostrarlos(valoresConseguidos)
sumaDados = sum(valoresConseguidos)

if sumaDados == 8:
    estadoJugador = 'Ganaste'
elif sumaDados == 7:
    estadoJugador = 'Perdiste'
else:
    estadoJugador = 'Continuar'
    print(f"Sigue jugando, encuentra al gran 8.")

contador = 1

while estadoJugador == 'Continuar': 
    valoresConseguidos = lanzar()
    mostrarlos(valoresConseguidos)
    sumaDados = sum(valoresConseguidos)

    if sumaDados == 8:
        estadoJugador = 'Ganaste'
    elif sumaDados == 7:
        estadoJugador = 'Perdiste'
    
    contador+= 1

print(f"El resultado es: {estadoJugador}")
print(f"Intentos: {contador}")

