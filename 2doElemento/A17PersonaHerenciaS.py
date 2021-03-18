#Creacion de clase padre
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad 

    def __str__(self):
        return "Nombre : "+self.nombre+" Edad: "+str(self.edad)

#creacion de una clase hija/o
class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo
    
#creacion de un objeto
persona = Persona("Jose Manuel",19)
#enviar impresion
print(persona)

