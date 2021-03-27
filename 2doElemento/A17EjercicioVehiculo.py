#Creacion de clase padre
class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas 

    def __str__(self):
        return "Color : "+self.color+" ruedas: "+str(self.ruedas)

#creacion de una clase hija/o
class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
    
    def __str__(self):
        return super().__str__() + "  velocidad : "+str(self.velocidad)+" km/hr"

#Creacion de clase hija/o
class Bici(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
    
    def __str__(self):
        return super().__str__() + "  tipo : "+str(self.tipo)

#creacion de un objeto
carro = Vehiculo("Rojo ",4 )
#enviar impresion
print(carro)

#Creacion de un objeto
coche = Coche("Negro ", 4 , 180)
#Enviamos a impresion el nuevo objeto
print(coche)

#Creacion de un objeto
bici = Bici("Negro ", 2 , "Montaña")
#Enviamos a impresion el nuevo objeto
print(bici)

