# EXCEPCONES
# Siempre debemos ser lo mas explicitos posibles a la hora de capturar un error

try: 
    numero = int(input("Ingresa un número: "))
    print( 1 / numero)

except ZeroDivisionError:
    # Captura errores de division entre cero
    print("No puedes dividir entre cero.")

except ValueError:
    # 
    print("Ingresa solo números por favor.")

except Exception:
    print("Algo ha ido mal.")

finally:
    # Para definir un bloque de código que siempre se ejecutará, sin importar si 
    # Se han presentado o no errores. 
    print("Do some cleanup here")



print("--------------------------------------")


try:
    archivo = open("datos.txt", "r")
except FileNotFoundError:
    # Para caturar error de cuando no se puede encontrar un archivo
    print("Error, no se pudo encontrar el archivo")
finally:
    # Se ejecuta si o si
    archivo.close()
    print("Proceso finalizado.")


print("--------------------------------------")

values = [10, 5, 6, 0, 9, 8, 2]

for value in values:
        
    try:
        print(10 / value)
    except:
        # Aqui solo estamos omitiendo el error y pasando a la siguiente division. No es una buena practica
        pass


print("--------------------------------------")

numero = input("Ingresa un numero: ")

try:
    print(5 / numero)
except Exception as e:
    # Captura cualquier posible error y lo guarda en la variable 'e'.
    # No se recomienda por buenas practicas, pero podemos tenerlo en cuenta.
    print(e)