import requests
import json
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




# Funcion para extraer los datos
def climaCiudades (lat, lon):

    
    api_key = "069f2a1737dadc173328a5735661062f"
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'
    #url = f'https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es'

    respuesta = requests.get(url)
    print(respuesta)


    # Convertimos a un .json
    # datos_clima = respuesta.json()
    datos_c = json.dumps(respuesta)
    print(respuesta)


# def ImprimirDatos():
    # Guardamos los datos específicos en variables:
    # Ubicacion
    pais = datos_c['sys']['country']
    ciudad = datos_c['name']
    nivel_mar = datos_c['main']['sea_level']


    # clima

    # clima = datos_clima['weather'][0]['description']
    # temperatura = round(datos_clima['main']['temp'] - 273.15, 1)    # Convertimos de Kelvin a Celsius
    # presion = datos_clima['main']['pressure']
    # humedad = datos_clima['main']['humidity']



    # viento = datos_clima['wind']['speed']
    # direccionViento = datos_clima['wind']['deg']


    # Mostrar datos del clima por pantalla

    print("\n-- DATOS DEL CLIMA ACTUALES --\n")

    print(f"PAÍS: {pais}.")
    print(f"UBICACIÓN: {ciudad}.")
    print(f"Altura a nivel del mar: {nivel_mar} msnm.\n")

    # print(f"Clima : {clima}.")
    # print(f"Temperatura actual: {temperatura} °C.")
    # print(f"Presión atmosférica: {presion}.")
    # print(f"Humedad: {humedad} (revisar).")
    # print(f"Velocidad del viento: {viento} Km/h.")
    # print(f"Dirección del viento: {direccionViento}°.")


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




# def Opc_3(city):

#     url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=es'

#     respuesta = requests.get(url)


#     # Convertimos a un .json
#     datos_clima = respuesta.json()
#     datos_c = json.dumps(datos_clima)
#     print(datos_c)


# Funcion para el menu general
def Menu():

    print("-- MENU --")
    print("| 1 | Ingresar coordenadas.") 
    print("| 2 | Seleccionar del listado de ciudades.")
    print("| 3 | Escribe tu ciudad.")
    print("| 0 | Salir.")

    opcion = input("\nSelecciona lo que deseas realizar:   ").lower().strip()


    if opcion == '1':
        lat = float(input("\nIngrese la latitud: "))
        lon = float(input("Ingrese la longitud: "))
        climaCiudades (lat, lon)

    elif opcion == '2':
        print("\nSeleccione de las siguientes ciudades: ")
        print("medellin, bogota, cali, londres, amsterdam, new york")
        city = input("\nEscriba la ciudad deseada:  ").lower().strip()
        Opc_2(city)

    # elif opcion == '3':
    #     ciudad = input("Escribe tu ciudad.").lower().strip()
    #     Opc_3(ciudad)

    elif opcion == '0':
        print("\nHa decidido salir del sistema.")


    else:
        print("Opcion invalida.")

Menu()



