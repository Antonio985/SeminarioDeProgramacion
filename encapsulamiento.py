#Creamos una clase con el nombre persona
class Persona:
            
    def __init__(self, nombre, edad):
        self.__nombre= nombre
        self.__edad = edad
    #Metodo get nombre
    def get__nombre(self):
        return self.__nombre
    #Metodo set Nombre
    def set__nombre(self, nombre):
        self.__nombre = nombre

    #Metodo get
    def get__edad(self):
        return self.__edad
    #Metodo set
    def set__edad(self, edad):
        self.__edad = edad

#Crea el objeto
persona1 = Persona("PEPE", 20)
print(persona1.get__nombre())
print(persona1.get__edad())
#Modificar el valor del atributo
persona1.set__nombre("PEPE GRILLO")
print(persona1.get__nombre())
print(persona1.get__edad())


