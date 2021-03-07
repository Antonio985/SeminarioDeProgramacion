print("********** BIENVENIDO AL MENU INTERACTIVO ********** ")
print("Que opcion desea Seleccionar? ")
print("1)Saludar")
print("2)Sumar dos numeros")
print("3)Salir del sistema")
Opcion = int( input() )

while Opcion<=3:
    if (Opcion==1):
        nombre = input("Enter your name : ") 
        print("Hola, mucho gusto ",nombre)
        break
    elif (Opcion==2):
        print("Ingrese primer numero: ")
        num1 = int( input() )
        print("Ingrese segundo numero: ")
        num2 = int( input() )
        print("La suma de sus numeros es :",num1+num2)
        break
    else:
        print("Saliendo del sistema....Gracias")
        break
    