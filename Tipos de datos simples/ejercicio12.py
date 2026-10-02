numerobarras = int(input("¿Cuantas barras de pan no se han vendido en el dia?"));
precio = float(3.49);
descuento = float(precio * (60/100));
descuentototal = float(numerobarras * (precio * (60/100) ) );
print (f"El precio habitual de una barra de pan es {precio}");
print (f"El descuento que se le hace por no ser fresca es {descuento} por cada barra de pan ");
print (f"El coste final de todas las barras de pan es {descuentototal}")
