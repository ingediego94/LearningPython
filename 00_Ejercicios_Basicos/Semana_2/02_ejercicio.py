'''
Asistente de productividad ⏳
Diseña un asistente que, según la hora actual y si es un día laboral o fin de semana, 
sugiera actividades como:
    "trabajar"
    "descansar"
    "hacer ejercicio"
Asegúrate de que los datos sean flexibles para futuras mejoras.
'''
from datetime import datetime

# VARIABLES
dateAndTime = datetime.now()
hourFormated = dateAndTime.strftime('%H:%M')
day = dateAndTime.strftime('%A').lower()
firstTwo = int(hourFormated[:2])

print("Today is: {}. It's {}".format(day, hourFormated))

def workingDays(hour):
    if 5 <= hour < 7:
        print('To wake up.')
    elif 7 <= hour < 8:
        print('To commute to the work.')
    elif 8 <= hour < 12:
        print('Working.')
    elif 12 <= hour < 14:
        print('Lunch time')
    elif 14 <= hour < 18:
        print('Working.')
    elif 18 <= hour < 20:
        print('Working out at the gym.')
    elif 20 <= hour < 21:
        print('Commuting to home.')
    elif ( 21 <= hour < 23) or ( 0 <= hour < 5 ):
        print('Sleeping.')
    else:
        print('Error.')

#def freeDays():


# ELECTION
if day == 'monday':
    print('Today is a working day.')
    workingDays(firstTwo)
elif day == 'tuesday':
    print('Today is a working day.')
    workingDays(firstTwo)
elif day == 'wednesday':
    print('Today is a working day.')
    workingDays(firstTwo)
elif day == 'thursday':
    print('Today is a working day.')
    workingDays(firstTwo)
elif day == 'friday':
    print('Today is a working day.')
    workingDays(firstTwo)
elif day == 'saturday':
    print('Today is a free day.')
    workingDays(firstTwo)
elif day == 'sunday':
    print('Today is a free day.')

else:
    print('We have an error.')


