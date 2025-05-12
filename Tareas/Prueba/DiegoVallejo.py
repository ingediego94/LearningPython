# Inventory management
# Made by: Diego Vallejo
# RIWI - Clan Hopper a.m.

"""
1. Añadir productos al inventario AL MENOS 5
2. Consultar productos en el inventario.
    Buscar por su nombre y mostrar: nombre, precio y cantidades disponibles
    Verificar si existe en el inventario o no
3. Actualizar precio de productos
    El precio debe ser un numero positivo   FALTA
4. Eliminar productos del inventario
    Confirmar su existencia antes de borrarlo
5. Calcular el valor total del inventario
    Debe ser preciso con dos decimales 

Hacer el codigo por funciones y comentarios 


"""

products = [
    {'name': 'pc gamer',
     'price' : 700.59,
     'quantity' : 8,
     'total' : 5604.72
     },
     {'name' : 'mouse',
      'price' : 40.31,
      'quantity' : 10,
      'total' : 403.1
     },
     {'name' : 'teclado mecánico',
      'price' : 85.47,
      'quantity' : 20,
      'total' : 1709.4
     },
     {'name' : 'celular',
      'price' : 199.4,
      'quantity' : 9,
      'total' : 1794.6
     },
     {'name' : 'hdmi premium',
      'price' : 25.15,
      'quantity' : 6,
      'total' : 150.9
     }
]

# AGREGAR FUNCION DE LOS MINIMO 5 PRODUCTOS

# 1. Function to add products
def addProducts():
    print('\n-- 📦  AGREGAR PRODUCTOS --')
    print('\nBienvenido al módulo para agregar nuevos productos. \nPor favor ingrese los siguientes datos del nuevo producto a ingresar en el inventario. ')
    productName = input('\nNombre del producto a agregar: ').strip().lower()
    productPrice = float(input('Precio del producto por unidad:  $ ').strip())
    productQuantity =int(input('Cantidad (unidades):  ').strip())

    # To add inputs to a new dictionary named 'product_dic'
    product_dic = {
        'name' : productName,
        'price' : productPrice,
        'quantity' : productQuantity
    }

    product_dic['total'] = productPrice * productQuantity

    # To add the previous dictinary to our list of products.
    products.append(product_dic)

    print(f"✅ El producto '{productName}' con valor $ {productPrice} y con {productQuantity}, se ha agregado exitosamente al inventario.")




# 2. Function to query a product
def productsQuery(listOfProducts):
    print('\n -- 🔍  CONSULTAR PRODUCTOS --')
    productToSearch = input('Escribe el nombre del producto deseas consultar:  ').lower().strip()

    for searcher in listOfProducts:
        if searcher['name'] == productToSearch:
            print("\netalles del producto buscado: \n")
            print(f"Producto: {searcher['name']}")
            print(f"Precio: $ {searcher['price']}")
            print(f"Cantidad: {searcher['quantity']}")
            break
    else:
        print(f"\nLo sentimos, el producto '{productToSearch}' no existe en el inventario.")




# 3. Function to update prices
def updateProducts(listOfProducts):
    print("\n-- CTUALIZAR PRODUCTOS --")
    productToSearch = input("\nIngresa el nombre del producto a actualizar:  ").lower().strip()

    for searcher in listOfProducts:
        if searcher['name'] == productToSearch:
            newPrice = float(input("Ingrese el nuevo precio del producto:  $ ").strip())
            searcher['price'] = newPrice
            searcher['total'] = searcher['price'] * searcher['quantity']

            print(f"\n ✅ Actualización exitosa de {productToSearch}, su nuevo precio es $ {newPrice}")
            break
    else: 
        print(f"\n🚫  El producto '{productToSearch}' no se encuentra registrado. Intente de nuevo.")




# 4. Function to delete productos 
def deleteProducts(listOfProducts):
    print("\n-- 🔥 BORRAR PRODUCTOS --")
    productToSearch = input("Nombre del producto a eliminar:  ").lower().strip()

    for searcher in listOfProducts:
        if searcher['name'] == productToSearch:
            print("\n   El producto fue encontrado en el inventario.")
            print("\n   Procesando requerimiento ...")
            listOfProducts.remove(searcher)
            print(f"\n  ✅ El producto '{productToSearch}' se ha eliminado correctamente.")
            break
    else:
        print(f"\n🚫  El producto '{productToSearch}' no se encuentra registrado en el inventario. \nIntente de nuevo.")
            



# 5. Function to calculate total accumulated value
def calculateTotalAccumulatedValue(listOfProducts):
    print(f"-- 🔢 CALCULAR VALOR TOTAL ACUMULADO DEL INVENTARIO --")
    print("\n ")







# General menu with all options
def menu():
        
    while True:
        
        # Shows the menu to user.
        print('\n-- MENU --')
        print('| 1 | Añadir productos al inventario.')
        print('| 2 | Consultar productos')
        print('| 3 | Actualizar precios.')
        print('| 4 | Eliminar productos. ')
        print('| 5 | Calcular el valor total del inventario:')
        print('| 0 | Salir.')

        try:    

            # request the operation to do, according to the menu.
           option = int(input('\nSelecciona la opción que deseas realizar (0 - 5):   ').strip())

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
               # logOff()
                pass
           
           else:
               print(f"\nHa seleccionado '{option}', la cual no es una opcion válida. \nIntente nuevamente.")
        
        except ValueError:
            print('\nHa ingresado una opción inválida. Por favor intente de nuevo.')


menu()