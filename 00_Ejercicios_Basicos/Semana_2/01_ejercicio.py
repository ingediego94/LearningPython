'''
1 Sistema de recomendaciones de películas 🎬
Crea un programa que recomiende una película basada en la edad del usuario y sus preferencias 
(acción, comedia, terror, etc.).
👉 Si el usuario es menor de 13 años, evita películas con clasificación para adultos.
'''
print("\nWELLCOME TO RIWI'S CINEMA\n")

age = int(input("What is your age? "))

option = 0

if age >= 14:
    print("1. Action movies")
    print("2. Horror movies.")
    print("3. Thriller movies.")
    print("4. ")
elif age <= 13:
    print("1. Adventure movies.")
    print("2. Animated movies.")
    print("3. Comedy movies")
    print("4. Documentals")
    option = int(input("What categorie do you chose? "))
    
    match option:
        case 1:
            print("- The amazing world of Gumbal.")
            print("- Jornuey to the center of the earth.")
            print("- Paddington in Peru.")
        case 2:
            print("- Ants 2")
            print("- Luca")
            print("- Mario Bross")
        case 3:
            print("- Daddy day care")
            print("- Home alone 4")
            print("- Despicable me")
        case 4:
            print("- The earth")
            print("- How it works?")
        case _:
            print("Incorrect option.")
        
else:
    print("Has ingresado una edad incorrecta.")