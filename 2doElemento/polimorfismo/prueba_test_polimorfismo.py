#importar clases
from empleados import Empleado
from gerente import Gerente

#definir metodo
def  imprimir_detalles(tipo_padre):
    print(tipo_padre)
    

    #creamos un objeto
    print(type(tipo_padre))
    
empleado = Empleado("Julian", 1200)

#para realizar la impresion por pantalla utilizaremos el metodo
imprimir_detalles(empleado)

#creacion de segundo objeto -- [Polimorfismo]
empleado = Gerente("Moises", 20000, "Gerencia Sistemas")
#enviaremos a impresion utilizando el metodo creado
imprimir_detalles(empleado)

