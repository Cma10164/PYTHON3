ingresos = int(input("Dime la cantidad de ahorros depositada en el banco: "));
formula = float((ingresos)*(1 + 0.04)**1);
formula1 = float((ingresos)*(1 + 0.04)**2);
formula2 = float((ingresos)*(1 + 0.04)**3);
print(f"La cantidad de ahorros el primer año es {formula:.2f} , el segundo año es {formula1:.2f} y el tercer año es {formula2:.2f}")