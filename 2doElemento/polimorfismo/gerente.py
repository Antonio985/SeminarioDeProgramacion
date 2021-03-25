#creamos clase
from empleados import Empleado
class Gerente(Empleado):
    def __init__(self, nombre, sueldo, departamento):
        super().__init__(nombre, sueldo)
        self.departamento =  departamento
    
    #mandamos a impresion
    def __str__(self):
        return super().__str__() + "  Departamento : "+ self.departamento