cesta = input("Introduce los productos de la cesta de la compra separados por comas: ")
cestalimpia = cesta.replace(', ', '\n').replace(',', '\n')
print("Los productos de tu cesta son:")
print(cestalimpia)
