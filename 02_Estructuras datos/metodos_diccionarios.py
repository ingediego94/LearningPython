# PRINCIPALES METODOS A USAR SOBRE DICCIONARIOS

# Diccionario base para pruebas
contactos = {
    'Ana': '1234',
    'Luis': '5678',
    'Marta': '9101'
}

# 1. .items() → recorrer claves y valores
print("\n1. .items()")
for nombre, telefono in contactos.items():
    print(f"Nombre: {nombre}, Teléfono: {telefono}")



# 2. .keys() → obtener solo las claves
print("\n2. .keys()")
for nombre in contactos.keys():
    print(f"Nombre: {nombre}")



# 3. .values() → obtener solo los valores
print("\n3. .values()")
for telefono in contactos.values():
    print(f"Teléfono: {telefono}")



# 4. .get() → obtener valor sin error si no existe la clave
print("\n4. .get()")
print(contactos.get('Ana'))          # Devuelve: 1234
print(contactos.get('Carlos'))       # Devuelve: None
print(contactos.get('Carlos', 'No encontrado'))  # Devuelve: No encontrado



# 5. .pop() → eliminar una clave y obtener su valor
print("\n5. .pop()")
telefono_eliminado = contactos.pop('Luis')
print(f"Luis eliminado, su número era: {telefono_eliminado}")
print("Diccionario actual:", contactos)



# 6. .popitem() → eliminar el último elemento insertado
print("\n6. .popitem()")
ultimo = contactos.popitem()
print(f"Elemento eliminado: {ultimo}")
print("Diccionario actual:", contactos)



# 7. .update() → actualizar con otro diccionario o pares clave-valor
print("\n7. .update()")
contactos.update({'Pedro': '7777', 'Ana': '8888'})  # Ana ya existía: se sobreescribe
print("Diccionario actualizado:", contactos)



# 8. .clear() → eliminar todos los elementos
print("\n8. .clear()")
contactos.clear()
print("Diccionario después de clear():", contactos)



# 9. .copy() → crear una copia del diccionario
print("\n9. .copy()")
contactos = {'Sara': '1111', 'Jorge': '2222'}
copia_contactos = contactos.copy()
print("Copia del diccionario:", copia_contactos)



# 10. .setdefault() → obtiene el valor si existe, si no, lo crea
print("\n10. .setdefault()")
contactos.setdefault('Laura', '3333')   # Se añade porque no existe
contactos.setdefault('Sara', '9999')    # No se cambia porque ya existe
print("Diccionario con setdefault:", contactos)
