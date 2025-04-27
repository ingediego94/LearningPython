# usa for para calcular el interes compuesto de una persona que invierte 10.000 en una cuenta que rinde el 8% de interes. Supon que la persona reinvierte los intereses. Calcula la cantidad de dinero al final de 10 años

year = 1
interes = 0.08
dinero = 10000.0
contador = 0

for x in range(9):
    dinero = dinero * (1 + interes)
    print(f"año {contador+1}: {round(dinero,2)}")
    year += 1