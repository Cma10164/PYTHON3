pizza = input("¿Quieres una pizza vegetariana?: ")
if pizza == "si" :
    ingrediente1=("Pimiento").lower()
    ingrediente2=("Tofu").lower()
    ingrediente = input("Que ingrediente le quiere añadir(Pimiento o Tofu): ")
    if ingrediente == ingrediente1:
        print(f"La pizza es vegetariana, los igredientes son mozzarella, tomate y {ingrediente1}")
    else:
        print(f"La pizza es vegetariana, los ingredientes son mozzarella, tomate y {ingrediente2}")
else :
    ingrediente3=("Jamon").lower()
    ingrediente4=("Peperoni").lower()
    ingrediente5=("Salmon").lower()
    ingredientev2 = input("Que ingrediente le quiere añadir(Jamon,Peperoni o Salmon): ")
    if ingredientev2 == ingrediente3:
        print(f"La pizza no es vegetariana, los igredientes son mozzarella, tomate y {ingrediente3}")
    elif ingredientev2 == ingrediente4:
        print(f"La pizza no es vegetariana, los ingredientes son mozzarella, tomate y {ingrediente4}")
    else :
        print(f"La pizza no es vegetariana, los ingredientes son mozzarella, tomate y {ingrediente5}")
