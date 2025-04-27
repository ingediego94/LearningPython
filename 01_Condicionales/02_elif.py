# Condicional if - else - elif

# En python no se usan las llaves {} para delimitar condicionales, aqui solo se usa la identacion.

num1 = int(input("Ingresa un numero: "))

if num1 > 0:
    print(f"El número {num1} es positivo.")
elif num1 == 0:
    print(f"El numero {num1} es igual a cero.")
else:
    print(f"El numero {num1} es negativo.")

print("Fin del programa.")