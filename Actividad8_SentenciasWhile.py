c=0 

while c<=10:
    c+=1
    print("Ahora el valor del C se a cambiado y en este momento vale : " ,c)


while c<=10:
    c+=1
    print("El valor de la C a cambiado y vale : ", c)
else:
    print("Se ha completado la iteración")
    
    
    

while c<=5:
    c+=1
    if (c==2):
          print("Este es un punto de ruptura")
          break
    print("Ahora el valor de C a cambiado y en este momento vale :", c)
else:
    print("Se ha completado la iteración y la c en este momento vale : ", c)
    

while c<=5:
    c+=1
    if (c==2):
          print("Este es un punto de ruptura")
          continue
    print("Ahora el valor de C a cambiado y en este momento vale :", c)
else:
    print("Se ha completado la iteración y la c en este momento vale : ", c)