precio = (input("Dime el precio del producto: "))
separador = precio.split('.');
euros = separador[0]
centimos = separador[1]

print(f"El precio es {euros} euros con {centimos} céntimos.")

