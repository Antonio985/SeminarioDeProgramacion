#Creamos una clase con el nombre persona
class Persona:
            
    def __init__(self, nombre, edad) -> none:
        self.__nombre= nombre
        self,edad=edad
    def get__nombre(self):
        return self.__nombre
    def set__nombre(self, nombre):
        self.__nombre = nombre

    #Metodo get
    def get__edad(self):
        return self.get__edad
    #Metodo set
    def set__edad(self, edad):
        self.__edad = edad

#Crea el objeto
persona1 = Persona("PEPE")
print(persona1.get__nombre())

#Modificar el valor del atributo
persona1.set__nombre("PEPE GRILLO")
print(persona1.get__nombre)

