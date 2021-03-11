#crearemos un clase -- dentro de la clase crearemos un metodo privado
class Persona:
    def __init__(self, nombre, apaterno, amaterno):
        self.nombre = nombre;
        self._apaterno = apaterno
        self.__amaterno = amaterno

    def metodo_publico(self):
        self.__metodo_privado()

    def __metodo_privado(self):
        print(self.nombre)
        print(self._apaterno)
        print(self.__amaterno)

    #metodo GET
    def get_apellido_materno(self):
        return self.__amaterno

    #Metodo SET
    def set_apellido_materno(self, amaterno):
        self.__amaterno = amaterno
    
#Creacion del objeto
persona1 = Persona("Julian","Flores","Figueroa")

#Enviamos impresion por pantalla usando metodo privado
#persona1.__metodo_privado()
#Como le hacemos para acceder a un metodo privado
#Accediendo por medio de un metodo publico
persona1.metodo_publico()

#¿puedo acceder de forma directa a los atributos?
print("*****Accediendo directamente a los atributos****")
print(persona1.nombre)
print(persona1._apaterno)
#print(persona1.__amaterno)
print(persona1.get_apellido_materno())


