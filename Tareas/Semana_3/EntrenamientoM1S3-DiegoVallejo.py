# ENTRENAMIENTO SEMANA 3, PYTHON.
# Presentado por: Diego Vallejo Z. 
# Riwi - Clan Hopper

# Programa de gestiónd e inventarios

def add_product(product_dict):
    name = input("Ingresa el producto: ")

    try: 
        
        price = float(input("Precio: "))
        productsQuantity = int(input("Cantidad: "))
    except ValueError:
        print("⚠️ El precio debe ser un numerico decimal y la cantidad un numero entero.")
        return

    product_dict[name] = {
        'precio' : price,
        'cantidad' : productsQuantity
    }

    print(f"✅ {name} ha sido agregado exitosamente al sistema.")

products = {}
add_product(products)

print("\n diccionario actual del productos: ")
print(products)