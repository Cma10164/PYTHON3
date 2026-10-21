pregunta = int(input("¿Cual es tu renta anual?: "))
if pregunta <= 10000 :
    print ("Tu tipo impositivo es 5%")
elif 10000 <= pregunta <=  20000 :
    print ("Tu tipo impostivo es 15%")
elif 20000 <= pregunta <=  35000 :
    print ("Tu tipo impostivo es 20%")
elif 35000 <= pregunta <=  60000 :
    print ("Tu tipo impostivo es 30%")
else :
    print ("Tu tipo impostivo es 45%")