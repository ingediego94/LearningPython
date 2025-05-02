edad = int(input("Ingresa tu edad: "))
es_ciudadano = input("¿Eres ciudadano? (si/no): ").lower() == "si"

if edad >= 18 and es_ciudadano:
    print("¡Estás habilitado para votar!")
else:
    print("No estás habilitado para votar.")
    
'''
es_ciudadano = input("¿Eres ciudadano? (si/no): ").lower() == "si"
Luego, comparas si la respuesta es exactamente igual a "si". Esta comparación devuelve un valor booleano:
    Si la respuesta es "si" (después de ser convertida a minúsculas), es_ciudadano será True.
    Si la respuesta es cualquier otra cosa (como "no", "no sé", o cualquier otra variante), es_ciudadano será False.
    
if edad >= 18 and es_ciudadano:: Esta es una condición compuesta que verifica dos cosas:

    1. edad >= 18: Verifica si la edad es mayor o igual a 18
    2. es_ciudadano: Verifica si la variable es_ciudadano es True
    
'''