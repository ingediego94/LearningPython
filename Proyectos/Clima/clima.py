import requests
import datetime


# Opcion de ciudades
ciudades = [
    {
        'city' : 'medellin',
        'lat': 6.24,
        'lon': -75.57,
    },
    {
        'city':'bogota',
        'lat': 4.66, 
        'lon': -74.07
    },
    {
        'city' : 'cali',
        'lat' : 3.40,
        'lon' : -76.52
    },
    {
        'city' : 'amsterdam',
        'lat' : 52.36,
        'lon' : 4.98
    },
    {
        'city' : 'londres',
        'lat' : 51.51,
        'lon' : -0.11
    },
    {
        'city' : 'new york',
        'lat' : 40.77,
        'lon' : -73.97
    }
]

api_key = "069f2a1737dadc173328a5735661062f"


# Funcion para extraer los datos
def climaCiudades (lat, lon):

    
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric&lang=es'
    #url = f'https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es'

    respuesta = requests.get(url)


    # Convertimos a un .json
    datos_en_json = respuesta.json()

    ImprimirDatos(datos_en_json)


def ImprimirDatos(datosJSON):
    # Guardamos los datos específicos en variables:
    # Ubicacion
    pais = datosJSON['sys']['country']
    ciudad = datosJSON['name']


    # clima

    clima = datosJSON['weather'][0]['description']
    temperatura = round(datosJSON['main']['temp'], 1)
    humedad = datosJSON['main']['humidity']


    viento = datosJSON['wind']['speed']
    direccionViento = datosJSON['wind']['deg']

    # Datos amanecer /atardecer
    amanecerData = datosJSON['sys']['sunrise']
    atardecerData = datosJSON['sys']['sunset']

    # Conversion datos amanecer / atardecer
    horaAmanecer = datetime.datetime.fromtimestamp(amanecerData)
    horaAmanecerFormateada = horaAmanecer.strftime("%H:%M")

    horaAtardecer = datetime.datetime.fromtimestamp(atardecerData)
    horaAtardecerFormateada = horaAtardecer.strftime("%H:%M")



    # Mostrar datos del clima por pantalla

    print("\n-- DATOS DEL CLIMA ACTUALES --\n")

    print(f"PAÍS: {pais}.")
    print(f"UBICACIÓN: {ciudad}.")
    print(f"Hora del amanecer: {horaAmanecerFormateada}. (Hora Colombia)")
    print(f"Hora del atardecer: {horaAtardecerFormateada}. (Hora Colombia)\n")

    print(f"Clima : {clima}.")
    print(f"Temperatura actual: {temperatura} °C.")
    print(f"Humedad: {humedad}%.")
    print(f"Velocidad del viento: {viento} m/s.")
    print(f"Dirección del viento: {direccionViento}°.\n")



# Funcion para la opcion 2 del menu.
def Opc_2(city):
    
    for ciudad in ciudades:
        if ciudad['city'] == city:

            lat = ciudad['lat']
            lon = ciudad['lon']
            climaCiudades (lat, lon)
            break

    else:
        print("ciudad no encontrada.")




def Opc_3(city):

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=es'

    respuesta = requests.get(url)


    # Convertimos a un .json
    datos_en_json = respuesta.json()

    ImprimirDatos(datos_en_json)





# Funcion para el menu general
def Menu():

    while True:
        print("-- MENU --")
        print("| 1 | Ingresar coordenadas.") 
        print("| 2 | Seleccionar del listado de ciudades.")
        print("| 3 | Escribe tu ciudad. ")
        print("| 0 | Salir.")

        opcion = input("\nSelecciona lo que deseas realizar:   ").lower().strip()

        try:
            if opcion == '1':
                lat = float(input("\nIngrese la latitud: "))
                lon = float(input("Ingrese la longitud: "))
                climaCiudades (lat, lon)

            elif opcion == '2':
                print("\nSelecciona de las siguientes ciudades: ")
                print("1. Medellin.   2. Bogotá.   3. Cali.    4. Londres.   5. Amsterdam.   6. New York")
                city = int(input("\nEscribe el número de ciudad deseada:  ").strip())
                
                city_op = ''

                if city == 1:
                    city_op = 'medellin'
                elif city == 2:
                    city_op = 'bogota'
                elif city == 3:
                    city_op = 'cali'
                elif city == 4:
                    city_op = 'londres'
                elif city == 5:
                    city_op = 'amsterdam'
                elif city == 6:
                    city_op = 'new york'
                
                
                Opc_2(city_op)

            elif opcion == '3':
                ciudad = input("Escribe tu ciudad:  ").lower().strip()
                Opc_3(ciudad)

            elif opcion == '0':
                print("\nHa decidido salir del sistema.")
                break


            else:
                print("Opcion invalida.")
        
        except ValueError:
            print("Error, revisa tu opcion, solo se permiten numeros.")
        except Exception:
            print("Revisa tu elección.")

Menu()



