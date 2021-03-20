#se solicitara un numero al usuario tomando en cuenta su valor de acuerdo al mes que corrresponda

mes = int(input("Ingrese un valor entre el 1 y 12 : "))

#creamos la estructura condicional para nuestro programa
if mes ==1 or mes == 2 or mes == 12:
    estacion="INVIERNO"
elif mes ==3 or mes == 4 or mes == 5:
    estacion="PRIMAVERA"
elif mes== 6 or mes == 7 or mes == 8:
    estacion="VERANO"
elif mes== 9 or mes == 10 or mes == 11:
    estacion="OTOÑO"
else:
    estacion="MES INCORRECTO"
    
print("La estacion corresponde a ",estacion," De acuerdo al mes : ",mes)
