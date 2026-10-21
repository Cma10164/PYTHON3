nombre = input("¿Cuál es tu nombre? ")
sexo = input("¿Cuál es tu sexo (M para mujer, H para hombre)? ")
if (sexo == "M" and nombre < "M") or (sexo == "H" and nombre > "N"):
    grupo = "A"
else:
    grupo = "B"
print(f"Te corresponde el grupo: {grupo}")