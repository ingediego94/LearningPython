# ENTRENAMIENTO SEMANA 3, PYTHON.
# Presentado por: Diego Vallejo Z. 
# Riwi - Clan Hopper

# Programa de gestión de inventarios
names = []
prices = []
quantitys = []
products = []
col1 = 'Producto'
col2 = 'Cantidad'
col3 = 'Precio'


#     ⚠️  ✅ 

# Function to add products

def add_product():
    name = input("Ingresa el nombre producto: ")
    price = float(input("Ingresa el precio del producto: "))
    quantity = int(input("Ingresa la cantidad de productos: "))

    product = {
        'nombre':name,
        'precio':price,
        'cantidad':quantity
    }

    products.append(product)

    print(f"Producto: {name} agregado con exito !")


# Function to search a product
def search_product(nombre):
    founded = False
    search = input("Nombre del producto a buscar: ")

    for name in names:
        if names["Producto"] == name:
            print(f"Producto: {pro}")





# Function to show the menu
def menu():
    while True:
        print(f"    MENU")
        print("|1| Agregar producto.")
        print("|2| Buscar producto.")
        print("|3| Actualizar precio producto.")
        print("|4| Eliminar producto.")
        print("|5| Calcular el valor total de inventario.")
        print("|6| Salir.\n")

        option = int(input("Selecciona una opción del 1 al 6 "))

        if option == 1:
            # agregar inputs por clean code
            add_product()
        elif option == 2:
            search_product()
        elif option == 3:
            update_price()
        elif option == 4:
            delete_product()
        elif option == 5:
            calculate_total_stock_price()
        elif option == 6:
            print("Gracias por utilizar nuestro sistema. \n¡Hasta luego!")
            print('*' * 60)
            break
        else:
            print('Opción no válida. Intenta de nuevo.')

menu()