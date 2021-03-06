#Envio a impresion dde pantalla, de los numeros pares
#Estos numeros estaran contenidos en un rango de valores

for i in range(10):
    if i%2==0:
        print(i)
        

for letra in "UNIVERSIDAD ESTATAL DE SONORA":
    if letra == "A":
        print(letra)
        break
    
    for j in range(10):
        if j%2!=0:
            continue
        print("El numero posicionado en este momento es PAR :", j)
        