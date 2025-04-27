# Como obtener la fecha y hora y cambiarle formato.

import datetime

ahora = datetime.datetime.now()

print(ahora)

print(type(ahora))

fechaYHora = ahora.strftime('%d/%m/%Y %H:%M:%S')
print(f"La fecha y hora actual es: {fechaYHora}")

fecha = ahora.strftime('%d/%m/%Y')
print(f"La fecha actual es: {fecha}")

hora = ahora.strftime('%H:%M:%S')
print(f"La hora actual es: {hora}")

mes = ahora.strftime('%d/%b/%Y')
print(f"La fecha con mes es: {mes}")

mesLargo = ahora.strftime('%d/%B/%Y')
print(f"La fecha con mes largo es: {mesLargo}")

dia = ahora.strftime('%a %d/%B/%Y')
print(f"La fecha con dia corto y mes largo es: {dia}")

diaLargo = ahora.strftime('%A %d of %B/%Y')
print(f"La fecha con dia largo y mes largo es: {diaLargo}")

