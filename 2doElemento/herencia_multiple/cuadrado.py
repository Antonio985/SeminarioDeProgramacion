#creamos una clase hija
#import Persona as person
#from Modulo_Persona import Persona 
#import modulos.modulo_persona import Persona
from figura_geometrica import FiguraGeometrica
import ColorF as colorf

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self,lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        ColorF.__init__(self, color)

    def area(self):
        return self.alto * self.ancho
