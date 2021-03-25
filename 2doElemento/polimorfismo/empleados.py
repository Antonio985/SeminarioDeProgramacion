#creamos clase
class  Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo
    
    #enviamos a impresion
    def __str__(self):
        return "Nombre : "+ self.nombre + " "+ str(self.sueldo)


        