import requests

lat = 10.64
lon = -71.63

api_key = "069f2a1737dadc173328a5735661062f"

url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'

respuesta = requests.get(url)


# Convertimos a un .json
datos_clima = respuesta.json()

# Guardamos los datos específicos en variables:
# Ubicacion
pais = datos_clima['sys']['country']

ciudad = datos_clima['name']

nivel_mar = datos_clima['main']['sea_level']


# clima

clima = datos_clima['weather'][0]['description']

temperatura = round(datos_clima['main']['temp'] - 273.15, 1)    # Convertimos de Kelvin a Celsius

presion = datos_clima['main']['pressure']

humedad = datos_clima['main']['humidity']



viento = datos_clima['wind']['speed']

direccionViento = datos_clima['wind']['deg']


#print(datos_clima)



# Mostrar datos del clima por pantalla

print("\n-- DATOS DEL CLIMA ACTUALES --\n")

print(f"PAÍS: {pais}.")
print(f"UBICACIÓN: {ciudad}.")
# print(f"Altura a nivel del mar: {nivel_mar} msnm.\n")

print(f"Clima : {clima}.")
print(f"Temperatura actual: {temperatura} °C.")
print(f"Presión atmosférica: {presion}.")
print(f"Humedad: {humedad} (revisar).")
print(f"Velocidad del viento: {viento} Km/h.")
print(f"Dirección del viento: {direccionViento}°.")

