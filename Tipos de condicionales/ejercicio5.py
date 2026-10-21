edad = int(input("Dime tu edad: "))
ingresos = float(input("Dime cuales son tus ingresos: "))
if edad >= 16 and ingresos >= 1000:
    print("debes tributar")
else:
    print("no debes tributar")