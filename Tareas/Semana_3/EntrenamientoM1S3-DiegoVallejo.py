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


# def add_product():
#     name = input("Ingresa el producto: ")

#     try: 
        
#         price = float(input("Precio: "))
#         productsQuantity = int(input("Cantidad: "))
#     except ValueError:
#         print("⚠️ El precio debe ser un numerico decimal y la cantidad un numero entero.")
#         return

#     product_dict[name] = {
#         'precio' : price,
#         'cantidad' : productsQuantity
#     }

#     print(f"✅ {name} ha sido agregado(a) exitosamente al sistema.")

# products = {}
# add_product(products)

# print("\n diccionario actual del productos: ")
# print(products)

# Function to add products

def add_product():
    name = input("Ingresa el nombre producto: ")
    price = float(input("Ingresa el precio del producto: "))
    quantity = int(input("Ingresa la cantidad de productos: "))

    # names.append(nombre)
    # prices.append(price)
    # quantitys.append(quantity)

    product = {
        'nombre':name,
        'precio':price,
        'cantidad':quantity
    }

    products.append(product)

    print(f"Producto: {name} agregado con exito !")



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