# Ejercicio 1 DISCORD: Formatear nombre completo
# Crea una función llamada formatear_nombre que reciba tres cadenas de texto: 
# nombre, segundo_nombre y apellido.
#La función debe devolver una sola cadena que contenga los tres nombres, 
# cada uno con la primera letra en mayúscula y el resto en minúscula, separados por espacios.
#Ejemplo:
#formatear_nombre("juan", "carlos", "perez") → "Juan Carlos Perez"


# Creacion de la funcion para formatear nombres
def formatear_nombre(nombreUno, nombreDos, apellidoUno):
    nombreUnoFormato = nombreUno.capitalize()
    nombreDosFormato = nombreDos.capitalize()
    apellidoUnoFormato = apellidoUno.capitalize()

    return f"{nombreUnoFormato} {nombreDosFormato} {apellidoUnoFormato}"

# Peticion de los datos al cliente
nombre1 = input("Cual es tu primer nombre? ")
nombre2 = input("Cual es tu segundo nombre? ")
apellido1 = input("Cual es tu primer apellido? ")

# Mostrar por pantalla aplicando la funcion
resultado = formatear_nombre(nombre1, nombre2, apellido1)

print(resultado)