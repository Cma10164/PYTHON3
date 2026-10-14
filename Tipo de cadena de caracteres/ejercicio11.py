producto = input("Nombre del producto: ")
precio = float(input("Precio unitario: "))
unidades = int(input("Número de unidades: "))
coste = precio * unidades
print(f"{producto}: {precio:09.2f}€ | {unidades:03d} unidades | Total: {coste:011.2f}€")
