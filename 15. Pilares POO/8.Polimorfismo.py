class Animales():
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def hablar (self):
        print(self.mensaje)
#polimorfismo hace referencia a la modificacion de un metodo que esta siendo heredado de otra clase
class Perro (Animales):
    def hablar(self):
        print ("Yo no hablo")

class Pez(Animales):
    def hablar(self):
        print ("Yo no hago ruido")

perru = Perro("Guau!")
perru.hablar()

animal = Animales ("Miau!")
animal.hablar()

pex = Pez("Nada")
pex.hablar()