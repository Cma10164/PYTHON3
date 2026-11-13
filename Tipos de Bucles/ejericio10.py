numero = int(input("Introduce un número entero: "))
primo = True
if numero < 2:
    primo = False
for divisor in range(2, numero):
    if numero % divisor == 0:
        primo = False
        break 
if primo:
    print(numero, "es primo")
else:
    print(numero, "no es primo")