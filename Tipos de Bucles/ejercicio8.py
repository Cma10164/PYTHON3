numero = int(input("Introduce un número entero: "))

for i in range(1, numero + 1):
    for j in range(2 * i - 1, 0, -2):
        print(j, end=" ")
    print()