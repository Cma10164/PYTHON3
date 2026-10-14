fechanacimiento = input("Dime tu fecha de nacimiento (dd/mm/aaaa): ")
partes = fechanacimiento.split('/');
dia = partes[0]
mes = partes[1]
año = partes[2]
print(f"Día: {dia}");
print(f"Mes: {mes}");
print(f"Año: {año}");
