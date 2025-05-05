# Usar un bucle para poblar una lista.

# Tradicional:

# Tradicional
cuadrados1 = []
for x in range(10):
    cuadrados1.append(x**2)
    
print(cuadrados1)

# List comprehension
cuadrados2 = [x **2 for x in range(10)]

print(cuadrados2)


# utilizando if en el list comprehencion

numbers = [1, 2, 3, 4, 5]
# filtering even numbers from a list
even_numbers = [num for num in range(1, 10) if num % 2 == 0 ]

print(even_numbers)


#  list comprehension con string
word = "Python"
vowels = "aeiou"

# find vowel in the string "Python"
result = [char for char in word if char in vowels]

print(result)
