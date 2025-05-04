'''
1 Sistema de recomendaciones de películas 🎬
Crea un programa que recomiende una película basada en la edad del usuario y sus preferencias 
(acción, comedia, terror, etc.).
👉 Si el usuario es menor de 13 años, evita películas con clasificación para adultos.
'''

# function to choose the movie only for kids
def chooseMovie_13():

    categorie = input("Choose the categorie that you want to watch: ").capitalize()

    match categorie:
        case "Comedy":
            print("\nComedy movies available to watch today: ")

            for movie_ in movies["Comedy"]:
                print('\t', movie_)

            
        case "Adventure":
            print("\tAdventure movies available to watch today: ")

            for movie_ in movies["Adventure"]:
                print('\t', movie_)

        case "Animated":
            print("\tAnimated movies available to watch today: ")
            
            for movie_ in (movies["Animated"]):
                print('\t', movie_)

        case "Documentals":
            print("\tDocumentals available to watch today: ")
            
            for movie_ in movies["Documentals"]:
                print('\t', movie_)
        case _:
            print("⚠️ You have choosen an icorrect option. Try again ¡")
    print("*" * 60)

# function to choose the movie for kids

def chooseMovie_all():

    categorie = input("Choose the categorie that you want to watch: ").capitalize()

    match categorie:
        case "Apocalypsis":

            print("\tApocalypsis movies available to watch today: ")

            for movie_ in movies["Apocalypsis"]:
                print('\t', movie_
                )

        case "Horror":
            
            print("\tHorror movies available to watch today: ")

            for movie_ in movies["Horror"]:
                print('\t', movie_)

        case "Action":
            
            print("\tAction movies available to watch today: ")

            for movie_ in movies["Action"]:
                print('\t', movie_)

        case "Documentals":

            print("\tDocumentals available to watch today: ")

            for movie_ in movies["Documentals"]:
                print('\t', movie_)

        case "Animated":

            print("\tAnimated movies available to watch today: ")

            for movie_ in movies["Animated"]:
                print('\t', movie_)

        case "Adventure":

            print("\tAdventure movies available to watch today: ")

            for movie_ in movies["Adventure"]:
                print('\t', movie_)

        case "Comedy":

            print("\tComedy movies available to watch today: ")
            
            for movie_ in movies["Comedy"]:
                print('\t', movie_)
        case _:
            print("⚠️ You have choosen an icorrect option. Try again ¡")
    print("*" * 60)


# List of movies and their categories
movies = {
    "Comedy" : [
        'Daddy day care', 
        'Home alone 4', 
        "Despicable me"
        ],

    "Adventure": [
        "The amazing world of Gumbal",
        "Jornuey to the center of the earth",
        "Paddington in Peru", 
        "A nanny bulletproof"
    ],

    "Animated" : [
        "Ants 2",
        "Luca",
        "Mario Bross"
    ],

    "Documentals" : [
        "The earth",
        "How it works?",
    ],

    "Action" : [
        "Hard to die",
        "Impossible mission",
        "RED",
        "The Last of Us"
    ],

    "Horror" : [
        "Chucky", 
        "The ancient mummy",
        "Emmily's Rose Exorcisim"
    ],

    "Apocalypsis" : [
        "The day after tomorrow",
        "Resident Evil 7",
        "28 days after"
    ]

}

#exit = False

while True:
    print("\n   WELLCOME TO RIWI'S CINEMA\n")
    print("     MENU\n")

    print("|1| To do a query.")
    print("|2| Exit.")

    option = int(input("\nInput your choice: \n"))

    if option == 1:

        age = int(input("What is your age? "))

        if 0 < age <= 99:

            if 0 <= age <= 13:
                print("\nWe have the following categories of movies available:\t")
                print("\tComedy")
                print("\tAdventure")
                print("\tAnimated")
                print("\tDocumentals")

                chooseMovie_13()

            elif 0 <= age <= 99:
                print("\nWe have the following categories of movies available:\t")
                print("\tAction")
                print("\tHorror")
                print("\tApocalypsis")
                print("\tComedy")
                print("\tAdventure")
                print("\tAnimated")
                print("\tDocumentals")

                chooseMovie_all()
                
            else:
                print("⚠️ You have choosen an incorrect option. Try again")
        else:
            print("You have writen a wrong age. Please verify and try again.")

    elif option == 2:
        print("Thank you!")
        break
