# Inventory management
# Made by: Diego Vallejo
# RIWI - Clan Hopper a.m.

"""
1. Añadir productos al inventario AL MENOS 5
2. Consultar productos en el inventario.
    Buscar por su nombre y mostrar: nombre, precio y cantidades disponibles
    Verificar si existe en el inventario o no

4. Eliminar productos del inventario
    Confirmar su existencia antes de borrarlo





"""

products = [
    # {'name': 'pc gamer',
    #  'price' : 700.59,
    #  'quantity' : 8,
    #  'total' : 5604.72
    #  },
    #  {'name' : 'mouse',
    #   'price' : 40.31,
    #   'quantity' : 10,
    #   'total' : 403.1
    #  },
    #  {'name' : 'teclado mecánico',
    #   'price' : 85.47,
    #   'quantity' : 20,
    #   'total' : 1709.4
    #  },
    #  {'name' : 'celular',
    #   'price' : 199.4,
    #   'quantity' : 9,
    #   'total' : 1794.6
    #  },
    #  {'name' : 'hdmi premium',
    #   'price' : 25.15,
    #   'quantity' : 6,
    #   'total' : 150.9
    #  }
]

products = []
quantityOfProducts = len(products)



# AGREGAR FUNCION DE LOS MINIMO 5 PRODUCTOS

# 1. Function to add products
def addProducts():

    while True:
        try:
            print('\n-- 📦  AGREGAR PRODUCTOS --')

            print('\nBienvenido al módulo para agregar nuevos productos. \nPor favor ingrese los siguientes datos del nuevo producto a ingresar en el inventario. ')
            productName = input('\nNombre del producto a agregar: ').strip().lower()
            productPrice = float(input('Precio del producto por unidad:  $ ').strip())
            productQuantity =int(input('Cantidad (unidades):  ').strip())

            if productPrice > 0.0 and productQuantity > 0:

                # To add inputs to a new dictionary named 'product_dic'
                product_dic = {
                    'name' : productName,
                    'price' : productPrice,
                    'quantity' : productQuantity
                }

                product_dic['total'] = productPrice * productQuantity

                # To add the previous dictinary to our list of products.
                products.append(product_dic)

                print(f"✅ El producto '{productName}' con valor $ {productPrice} y con {productQuantity} unidades, se ha agregado exitosamente al inventario.")
                print(products)
                print('-' * 100)
                break
            
            else:
                print("El precio debe ser un número real positivo y la cantidad un entero positivo.")
                print('-' * 100)
        except ValueError:
            print("Error, intenta de nuevo.")




# 2. Function to query a product
def productsQuery(listOfProducts):
    print('\n -- 🔍  CONSULTAR PRODUCTOS --')




    if quantityOfProducts != 0:
        productToSearch = input('Escribe el nombre del producto deseas consultar:  ').lower().strip()

        for searcher in listOfProducts:
            if searcher['name'] == productToSearch:
                print("\nDetalles del producto buscado: \n")
                print(f"Producto: {searcher['name']}")
                print(f"Precio: $ {searcher['price']}")
                print(f"Cantidad: {searcher['quantity']}")
                print(f"Total invertido en este producto: $ {searcher['total']}")
                print('-' * 100)
                break
        else:
            print(f"\nLo sentimos, el producto '{productToSearch}' no existe en el inventario.")
            print('-' * 100)

    elif quantityOfProducts == 0:
        print("\nEl inventario de productos está vacío. No hay productos que consultar.")
        print(products)
        print(len(products))
        print('-' * 100)


# 3. Function to update prices
def updateProducts(listOfProducts):
    print("\n-- 🔄 ACTUALIZAR PRODUCTOS --")

    if quantityOfProducts == 0: 
        print("No hay productos en el inventario que actualizar. La base de datos está vacía.")
        print('-' * 100)

    elif quantityOfProducts >= 1:

        productToSearch = input("\nIngresa el nombre del producto a actualizar:  ").lower().strip()

        for searcher in listOfProducts:
            if searcher['name'] == productToSearch:
                newPrice = float(input("Ingrese el nuevo precio del producto:  $ ").strip())
                if newPrice > 0:
                    searcher['price'] = newPrice
                    searcher['total'] = searcher['price'] * searcher['quantity']

                    print(f"\n ✅ Actualización exitosa de {productToSearch}, su nuevo precio es $ {newPrice}")
                    print('-' * 100)
                    break
                else: 
                    print(f"El precio ingresado debe ser un número positivo.")
                    print('-' * 100)
                    break
        else: 
            print(f"\n🚫  El producto '{productToSearch}' no se encuentra registrado. Intente de nuevo.")
            print('-' * 100)




# 4. Function to delete productos 
def deleteProducts(listOfProducts):
    
    print("\n-- 🔥 BORRAR PRODUCTOS --")

    if quantityOfProducts == 0:
        print("El inventario de productos está vacío, no hay productos por borrar.")
        print('-' * 100)
    
    elif quantityOfProducts >= 1:
        productToSearch = input("Nombre del producto a eliminar:  ").lower().strip()

        for searcher in listOfProducts:
            if searcher['name'] == productToSearch:
                print("\n   El producto fue encontrado en el inventario.")
                print("\n   Procesando requerimiento ...")
                listOfProducts.remove(searcher)
                print(f"\n  ✅ El producto '{productToSearch}' se ha eliminado correctamente.")
                print('-' * 100)
                break
        else:
            print(f"\n🚫  El producto '{productToSearch}' no se encuentra registrado en el inventario. \nIntente de nuevo.")
            print('-' * 100)    



# 5. Function to calculate total accumulated value
def calculateTotalAccumulatedValue(listOfProducts):
    
    print(f"-- 🔢 CALCULAR VALOR TOTAL ACUMULADO DEL INVENTARIO --")

    if quantityOfProducts == 0:
        print('La base de datos está vacía, no hay productos en inventario para calcular su valor.')
        print('-' * 100)

    elif quantityOfProducts >= 1:

        #totalValue = sum(listOfProducts['total'])
        totalValue = sum([dictionary['total'] for dictionary in listOfProducts])

        print(f"\n El valor total invertido en el inventario es de: $ {round(totalValue, 2)}")
        print('-' * 100)





# General menu with all options
def menu():
        
    while True:
        
        # Shows the menu to user.
        print('\n-- 📝 MENU --')
        print('| 1 | Añadir productos al inventario.')
        print('| 2 | Consultar productos')
        print('| 3 | Actualizar precios.')
        print('| 4 | Eliminar productos. ')
        print('| 5 | Calcular el valor total del inventario:')
        print('| 0 | Salir.')

        try:    

            # request the operation to do, according to the menu.
           option = int(input('\nSelecciona la opción que deseas realizar (0 - 5):   ').strip())
           print('-' * 100)

            # 1. Option to add products.
           if option == 1:
                addProducts()
               

           # 2. Option to products query.
           elif option == 2:
                productsQuery(products)

           
           # 3. Option to update products.
           elif option == 3:
                updateProducts(products)
               
           
           # 4. Option to delete products.
           elif option == 4:
                deleteProducts(products)
               
           
           # 5. Option to calculate total inventory.
           elif option == 5:
                calculateTotalAccumulatedValue(products)
               
           
           # 6. Option to exit.
           elif option == 0:
                print(f"\n -- ❌ SALIDA --")
                print("\n Gracias. Vuelve pronto. ")
                print('=' * 100)
                break
           
           else:
                print(f"\nHa seleccionado '{option}', la cual no es una opcion válida. \nIntente nuevamente.")
        
        except ValueError:
            print('\nHa ingresado una opción inválida. Por favor intente de nuevo.')
            print('-' * 100)





menu()

