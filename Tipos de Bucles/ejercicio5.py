cantidad = float(input("Introduce la cantidad a invertir: "))
interes = float(input("Introduce el interés anual (%): "))
años = int(input("Introduce el número de años: "))

for i in range(1, años + 1):
    cantidad = cantidad + cantidad * interes / 100
    print("Año", i, ":", round(cantidad, 2), "€")