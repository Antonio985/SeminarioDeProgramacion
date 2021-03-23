#creamos la clase padre
class Terrestre:
    def desplazarTierra(self):
        print("El cocodrilo se dezplaza sobre la tierra")

class Acuatico:
    def desplazarAgua(self):
        print("El cocodrilo se dezplaza sobre el agua")

#creamos la clase hijo
class Cocodrilo(Terrestre, Acuatico):
    pass

c = Cocodrilo()
c.desplazarTierra()
c.desplazarAgua()

