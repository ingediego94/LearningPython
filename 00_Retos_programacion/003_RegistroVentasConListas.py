# Sistema de ventas con productos precargados ya con su precio para seleccionar. 
# Permite el registro del usuario, ver los productos agregados al carrito,
# Editar los productos seleccionados así como sus cantidades.
# Al final presenta la factura de lo adquirido.

usuario = []

productos = [
    ["Pollo", 30500,34, "Carne"],
    ["Cebolla", 1500,2, "Vegales"],
    ["Arroz", 2500,79, "Cereal"],
    ["Quinua", 5400,9, "Cereal"]
]

carro = []

print()
print("==" * 25)
print("||              Carro de compras              ||")
print("==" * 25)

try:
    while True:
        print("-" * 50)
        print("                      MENU                      ")
        print("-" * 50)
        print()

        print("[1] Registra el usuario o actualiza sus detalles.")
        print("[2] Agregar productos al carrito de compras.")
        print("[3] Ver el carrito de compras.")
        print("[4] Actualizar el carro de compras.")
        print("[5] Remover productos del carro de compras.")
        print("[6] Salir del programa.")

        opcion = int(input("->"))

        if opcion == 1: 
            print("-" * 30)
            if not usuario:
                nombre = input("Ingresa tu nombre: ")
                apellido = input("Escribe tu apellido: ")
                documento = input("Escribe tu númpero de documento: ")

                usuario.append(nombre)
                usuario.append(apellido)
                usuario.append(documento)

                print("Usuario registrado exitosamente")
            
            else:
                print("El usuario ya está registrado, puedes editarlo si lo deseas.")
                print()
                nombre = input("Escribe tu nombre: ")
                apellido = input("Escribe tu apellido: ")
                documento = input("Escribe tu número de documento: ")

                usuario[0] = nombre
                usuario[1] = apellido
                usuario[2] = documento
                
                print("Información del usuario actualizada correctamente.")
        
        elif opcion == 2:
            print("-" * 50)
            print("Productos disponibles")
            print("-" * 50)
            contar = 0
            for i in productos:
                print(f"[{contar + 1}] {i[0]} - ({i[1]})")
                contar += 1
            producto = int(input("Ingresa el ID del producto que deseas agregar: "))
            producto = (producto - 1)
            print(f"    Cuantas unidades de '{productos[producto][0]}' deseas agregar?")
            cantidad = int(input("(e.g., 7 ->)"))
            carro_item = []
            carro_item.append(productos[producto][0])
            carro_item.append(productos[producto][1])
            carro_item.append(cantidad)
            carro_item.append((productos[producto][1]*cantidad))
            carro_item.append(productos[producto][2])
            carro.append(carro_item)
            print()
            print("PRODUCTO AGREGADO AL CARRITO")
            print()
        elif opcion == 3:
            print("-" * 50)
            if not carro:
                print("El carro está vacío.")
            else:
                print("-" * 35)
                print("Carro actual")
                print("-" * 35)
                subtotal = 0
                for i in carro:
                    print(f"{i[0]} ({i[1]}) * {i[2]} = {i[3]}")
                    subtotal += i[3]
                print("-" * 35)
                impuesto = subtotal * 0.19
                total = (subtotal + impuesto)

                print("SUBTOTAL = ", subtotal)
                print("Impuestos 19% = ", impuesto)
                print("TOTAL = ", total)
                print("-" * 35)
        elif opcion == 4:
            print("-" * 50)
            if not carro:
                print("El carro está vacio")
            else:
                print("Carro")
                contar = 0
                for i in carro:
                    print(f"[{contar + 1}] {i[0]}({i[1]}) * {i[2]} = {i[3]}")
                    contar += 1
                producto = int(input("Ingresa el ID del producto que deseas actualizar "))
                producto = (producto - 1)
                nueva_cantidad = int(input(f"   Cuantas unidades de '{carro[producto][0]}' deseas? "))
                carro[producto][2] = nueva_cantidad
                carro[producto][3] = (carro[producto][1] * nueva_cantidad)
                print()
                print("PRODUCTO ACTUALIZADO CORRECTAMENTE")
                print()
        elif opcion == 5:
            print("-" * 50)
            if not carro:
                print("El carro esta vacio")
            else:
                print("Carro")
                contar = 0
                for i in carro:
                    print(f"[{contar + 1}] {i[0]}({i[1]}) * {i[2]} = {i[3]}")
                    contar += 1
                producto = int(input("Ingresa el ID del producto que deseas eliminar: "))
                producto = (producto - 1)
                del carro[producto]
                print()
                print("PRODUCTO ELIMINADO EXITOSAMENTE.")
                print()
        elif opcion == 6:
            print("Fue un placer servirte.")
            exit()
        else:
            print("La opcion ingresada no se encuentra en el menu.")                    
except ValueError:
    print("Has ingresado una entrada invalida.")