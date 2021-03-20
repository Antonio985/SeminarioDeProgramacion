#sentencia If-ELSE

condicion = True

#Evaluar con una estructura condicional IF

if condicion:
    print("La condicion es VERDADERA")
else:
    print("La condicion es FALSA")

#Uso de el - if
if(condicion == True):
    print("La condicion es verdadera , de modo  Explicito")
elif(condicion == False):
    print("La condicion es falsa , de modo explicito")
else:
    print("Expresion no reconocida")


#Se pedira al usuario ingresar un valor del 1 al 3

numero = int(input("Proporciona un numero entre 1 y 3 "))

#evaluamos
if(numero == 1):
    numeroTexto="Numero UNO"
elif(numero == 2):
    numeroTexto="Numero DOS"
elif(numero == 3):
    numeroTexto="Numero TRES"
else:
    numeroTexto="Valor Fuera de Rango"
print(numeroTexto)

