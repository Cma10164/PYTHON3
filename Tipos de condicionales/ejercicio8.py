base = 2400

puntuacion = float(input("Introduce tu puntuación de evaluación (0.0, 0.4, 0.6 o más): "))

valida = True

if puntuacion == 0.0:
    nivel = "Inaceptable"
elif puntuacion == 0.4:
    nivel = "Aceptable"
elif puntuacion >= 0.6:
    nivel = "Meritorio"
else:
    valida = False

if valida:
    dinero_recibido = base * puntuacion
    print(f"Tu nivel de rendimiento es: {nivel}")
    print(f"Cantidad de dinero que recibirás: {dinero_recibido:,.2f}€")
else:
    print("Error: La puntuación introducida no es válida. Debe ser 0.0, 0.4 o igual/mayor a 0.6.")
