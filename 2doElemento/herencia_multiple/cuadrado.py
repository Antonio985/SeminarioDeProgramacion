#creamos una clase hija
#import Persona as person
#from Modulo_Persona import Persona 
#import modulos.modulo_persona import Persona
from figura_geometrica import FiguraGeometrica
from colorf import ColorF

class Cuadrado(FiguraGeometrica, ColorF):
    def __init__(self,lado , colorf):
        FiguraGeometrica.__init__(self, lado, lado)
        ColorF.__init__(self, colorf)

    def area(self):
        return self.alto * self.ancho
