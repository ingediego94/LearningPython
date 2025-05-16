# Ejercicio 3: DISCORD  Verificar contraseña segura
# Descripción:
# Crea una función llamada es_contrasena_segura que reciba un texto (string) 
# como parámetro y devuelva True si la contraseña es segura, o False si no lo es.
# Una contraseña se considera segura si cumple con lo siguiente:
    # Tiene al menos 8 caracteres.
    # Contiene al menos una letra mayúscula.
    # Contiene al menos un número.


# Definimos la funcion:
def es_contrasena_segura (contrasenna):
    contineMayuscula = any(c.isupper() for c in contrasenna)
    contieneNumero = any(c.isdigit() for c in contrasenna)

    if len(contrasenna) >= 8 and contineMayuscula and contieneNumero:
        return True
    else:
        return False


# Pedimos la contraseña al usuario.
password = input("Ingresa tu contraseña: \n\t")

# Evaluamos la contrasena
esSegura = es_contrasena_segura(password)

if esSegura:
    print("Contraseña segura porque:")
    print("\t1. Tiene al menos 8 caracteres.")
    print("\t2. Tiene al menos una letra mayúscula.")
    print("\t3. Tiene al menos un número.")
else:
    print("La contraseña no es segura.")