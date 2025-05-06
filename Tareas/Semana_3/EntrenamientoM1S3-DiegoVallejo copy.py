# ENTRENAMIENTO SEMANA 3, PYTHON.
# Presentado por: Diego Vallejo Z. 
# Riwi - Clan Hopper

# Programa de gestión de inventarios

products = []


#     ⚠️   

# Function to add products

def add_product():
    name = input("Ingresa el nombre producto: ")
    price = float(input("Ingresa el precio del producto: "))
    quantity = int(input("Ingresa la cantidad de productos: "))

    product_dic = {
        'producto': name,
        'precio': price,
        'cantidad': quantity
    }

    #agregar el diccionario a la lista
    products.append(product_dic)

    print(f"\n✅ Producto: {name} agregado(a) con éxito !\n")

    # Imprime cada uno de los registros:

    # for i, producto in enumerate(products, 1):
    #     print(f"\nProducto {i}:")
    #     for clave, valor in producto.items():
    #         print(f"{clave}: {valor}")

    


# Function to search a product
def search_product(list_of_products):
    founded = False
    search = input("Nombre del producto a buscar: \n").lower()

    for product_searcher in list_of_products:
        if product_searcher['producto'] == search:
            print(f"\nProducto: {product_searcher['producto']} | Precio: ${product_searcher ['precio']} | Cantidad: {product_searcher['cantidad']} unidades.")
            founded = True
            break
    if not founded:
        print("El producto no se encuentra registrado en la base de datos.")




# Function to show the menu
def menu():
    while True:
        print(f"\n    MENU")
        print("|1| Agregar producto.")
        print("|2| Buscar producto.")
        print("|3| Actualizar precio producto.")
        print("|4| Eliminar producto.")
        print("|5| Calcular el valor total de inventario.")
        print("|6| Salir.\n")

        option = int(input("Selecciona una opción del 1 al 6: \n"))



        if option == 1:
            # agregar inputs por clean code
            add_product()
        elif option == 2:
            search_product(products)
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
            print('Opción no válida. "Intenta de nuevo.')




menu()