for i in range(1, 10):
    if i % 2 != 0:  # Omite números impares
        continue
    if i % 3 == 0:  # Para en el primer número divisible por 3
        print(f"Primer número divisible por 3: {i}")
        break