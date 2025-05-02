# Tradicional
cuadrados1 = []
for x in range(10):
    cuadrados1.append(x**2)
    
print(cuadrados1)



# List comprehension
cuadrados2 = [x **2 for x in range(10)]

print(cuadrados2)

'''
lo que hace el x**2 de la expresion [x **2 for x in range(10)]
es ingresar esos datos a la lista sin necesidad de hacer el 
cuadrados.append(x**2)
'''