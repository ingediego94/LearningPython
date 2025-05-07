# ENTRENAMIENTO SEMANA 3, PYTHON.
# Presentado por: Diego Vallejo Z. 
# Riwi - Clan Hopper

# Programa de gestión de inventarios

products = []


#     ⚠️   

# Function to add products

def add_product():
    name = input("Ingresa el nombre producto:  ").lower()
    price = float(input("Ingresa el precio del producto:  $ "))
    quantity = int(input("Ingresa la cantidad de productos:  "))

    product_dic = {
        'producto': name,
        'precio': price,
        'cantidad': quantity
    }

    product_dic['total'] = price * quantity

    #agregar el diccionario a la lista
    products.append(product_dic)
    print(product_dic)
    print(f"\n✅ Producto: {name} agregado(a) con éxito !")

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
            print(f"\n🔍 Producto: {product_searcher['producto']} | Precio: ${product_searcher ['precio']} | Cantidad: {product_searcher['cantidad']} unidades.")
            founded = True
            break
    if not founded:
        print("El producto no se encuentra registrado en la base de datos.")


# Function to update pr
def update_price(list_of_products):
    search = input("Nombre del producto a actualizar: \n").lower()
    
    for product_searcher in list_of_products:
        if search == product_searcher['producto']:
            #update_product = input("Actualiza el nombre del producto:    ").lower()
            update_price = float(input("Actualiza su precio:    $"))
            update_quatity = int(input("Actualiza su cantidad:  "))

            #product_searcher['producto'] = update_product
            product_searcher['precio'] = update_price
            product_searcher['cantidad'] = update_quatity

            print("\n✅ Actualización exitosa del producto.")
            break


# Function to delete products
def delete_product(list_of_products):
    
    search = input("Busca por su nombre el producto que deseas eliminar:  ").lower()

    for product_searcher in list_of_products:
        if search == product_searcher['producto']:
            del product_searcher['cantidad']
            del product_searcher['precio']
            del product_searcher['producto']
            break
    # mejorar el eliminar los diccionarios vacios.
    print(list_of_products)


def calculate_total_stock_price(list_of_products):
    total = sum(product1['total'] for product1 in list_of_products)
    print(f"El total de todo el inventario es: {total}")


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
            update_price(products)
        elif option == 4:
            delete_product(products)
        elif option == 5:
            calculate_total_stock_price(products)
        elif option == 6:
            print("Gracias por utilizar nuestro sistema. \n¡Hasta luego!")
            print('=' * 50)
            break
        else:
            print('Opción no válida. "Intenta de nuevo.')




menu()