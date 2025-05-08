# ENTRENAMIENTO SEMANA 3, PYTHON.
# Programa de gestion de inventarios.
# Presentado por: Diego Vallejo Z. 
# Riwi - Clan Hopper


# NOTA: El programa requiere un usuario y contraseña, los cuales son:
    # Usuario:      Admin
    # Contraseña:   admin123*



# We use datetime to get the date and the hour of use.
from datetime import datetime

dateAndTime = datetime.now()
dateFormated = dateAndTime.strftime("Fecha: %Y-%m-%d                     Hora: %H:%M")


# Tuple to create a validation through user and password
credentials = ('Admin', 'admin123*')


# List to store all data has been inputted on the console
products = []


# Variables to print with format
col1 = "PRODUCTO"
col2 = "PRECIO ($)"
col3 = "CANTIDAD (un)"
col4 = "TOTAL ($)"
width = 20



# Function to add products
def add_product():
    
    print(f"             📦   AGREGAR PRODUCTOS")
    name = input("Ingresa el nombre producto:  ").lower()
    price = float(input("Ingresa el precio del producto:  $ "))
    quantity = int(input("Ingresa la cantidad de productos:  "))

    product_dic = {
        'producto': name,
        'precio': price,
        'cantidad': quantity
    }

    product_dic['total'] = price * quantity

    # To add dictionary to the list
    products.append(product_dic)
    
    print(f"\nResumen de los datos agregados:\n{product_dic}")
    print(f"\n✅ Producto: {name} agregado(a) con éxito !")




# Function to search a product
def search_product(list_of_products):
    print("\n           🔍   BÚSQUEDA DE PRODUCTOS POR NOMBRE")
    founded = False
    search = input("\nNombre del producto a buscar: \n").lower()

    for product_searcher in list_of_products:
        if product_searcher['producto'] == search:

            print("\n                           🔍   BÚSQUEDA DE PRODUCTOS")

            print(f"{col1.center(width)} | {col2.center(width)} | {col3.center(width)} | {col4.center(width)}")
            print(f"{product_searcher['producto'].center(width)}  {str(product_searcher['precio']).center(width)}  {str(product_searcher['cantidad']).center(width)}  {str(product_searcher['total']).center(width)}")
            founded = True
            break

    if not founded:
        print("⚠️  El producto no se encuentra registrado en la base de datos.")




# Function to update products
def update_price(list_of_products):

    print(f"             🔄   ACTUALIZAR PRODUCTOS")

    search = input("\nNombre del producto a actualizar: \n").lower()

    # This verify if any dictionary value is the same to search, if this is true, continue with the next instructions
    if any(product['producto'] == search for product in list_of_products):
    
        for product_searcher in list_of_products:
            if search == product_searcher['producto']:
                #update_product = input("Actualiza el nombre del producto:    ").lower()
                update_price = float(input("Actualiza su precio:    $"))
                update_quatity = int(input("Actualiza su cantidad:  "))

                #product_searcher['producto'] = update_product
                product_searcher['precio'] = update_price
                product_searcher['cantidad'] = update_quatity
                product_searcher['total'] = product_searcher['precio'] * product_searcher['cantidad']

                print("\n✅ Actualización exitosa del producto.")
                print('-' * 50)
                break
    else:
        print(f"\n🚫  El producto '{search}' no se encuentra registrado. Intente nuevamente.")




# Function to delete products
def delete_product(list_of_products):
    
    print(f"             🔥   ELIMINAR PRODUCTOS")
    search = input("Nombre del producto a eliminar:  ").lower()

    # This verify if any dictionary value is the same to search, if this is true, continue with the next instructions
    if any(product['producto'] == search for product in list_of_products):

        for product_searcher in list_of_products:
            if search == product_searcher['producto']:
                list_of_products.remove(product_searcher)

                break

        print("\n✅ El producto ha sido eliminado correctamente !")

    
    else:
        print(f"\n🚫  El producto '{search}' no se encuentra registrado. Intente nuevamente.")




def calculate_total_stock_price(list_of_products):

    print(f"       🔢   TOTAL EN INVENTARIO DE PRODUCTOS")

    #total = sum(map(lambda product: product['total'], list_of_products))   # Lambda function
    total = sum(product1['total'] for product1 in list_of_products)
    print(f"\nEl total de todo el inventario es:  $ {total: .2f}")





def detail_entire_db(list_of_products):

    print(f"                            📋   REGISTRO TOTAL DE PRODUCTOS\n")

    print(f"{col1.center(width)} | {col2.center(width)} | {col3.center(width)} | {col4.center(width)}")

    for i in list_of_products:
        print(f"{i['producto'].center(width)}  {str(i['precio']).center(width)}  {str(i['cantidad']).center(width)}  {str(i['total']).center(width)}")
    
    for i in list_of_products:
        print(*i.values())



# Function to show the menu and to request the option
def menu():
    while True:
        print(f"\n             📝  MENU")
        print("| 1 | 📦 Agregar producto.")
        print("| 2 | 🔍 Buscar producto.")
        print("| 3 | 🔄 Actualizar precio producto.")
        print("| 4 | 🔥 Eliminar producto.")
        print("| 5 | 🔢 Calcular el valor total de inventario.")
        print("| 6 | 🔍 Ver toda la base de datos.")
        print("| 0 | ❌ Salir.\n")

        

        try:
            option = int(input("Selecciona una opción del 1 al 6: \n"))

            if option == 1:
                add_product()
            elif option == 2:
                search_product(products)
            elif option == 3:
                update_price(products)
            elif option == 4:
                delete_product(products)
            elif option == 5:
                calculate_total_stock_price(products)
            elif option == 6:
                detail_entire_db(products)
            elif option == 0:
                print(f"\n             ❌ SALIDA")
                print("\nGracias por utilizar nuestro sistema. \n           ¡Hasta luego!")
                print(f"\nFecha y hora de salida \n{dateFormated}")
                print('=' * 50)
                break
            else:
                print('Opción no válida. "Intenta de nuevo.')

        except ValueError:
            print("Ha ingresado una opcion inválida. Puedes intentar de nuevo.")


print("\n         BIENVENIDO AL REGISTRO DE INVENTARIO")
user = input("\n🙍 Usuario:     ")
password = input("🔒 Contraseña:  ")


# Resquest of user and password to enter to the system

if user == credentials[0] and password == credentials[1]:

    menu()

else:
    print("\nCredenciales inválidas. Intenta de nuevo.\n")

