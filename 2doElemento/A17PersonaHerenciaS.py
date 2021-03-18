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
    
    def __str__(self):
        return super().__str__() + "  Sueldo : "+str(self.sueldo)

#creacion de un objeto
persona = Persona("Jose Manuel ",19 )
#enviar impresion
print(persona)

#Creacion de un objeto
empleado = Empleado("Maria Ines ", 18 , 15500.63)
#Enviamos a impresion el nuevo objeto
print(empleado)
