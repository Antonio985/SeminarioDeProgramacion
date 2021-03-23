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
        return super().__str__() + "  velocidad : "+str(self.velocidad)

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
