'''
Crear una clase llamada Marino(), con un metodo que sea hablar, en donde muestre un mensaje que diga "Hola...". Luego, crear una clase Pulpo() que herede Marino, pero modificar el mensaje de hablar por "Soy un Pulpo". Por ultimo, crear una clase Foca(), heredada de Marino, pero que tenga un atributo nuevo llamado mensaje y que muestre ese mensaje como parametro
'''

class Marino():
    def hablar(self):
        print ("Hola...")

class Pulpo(Marino):
    def hablar(self):
        print ("Soy un pulpo")

class Foca(Marino):
    def hablar(self, mensaje):
        self.mensaje = mensaje #invoco el atributo de mensaje que viene del metodo hablar de la clase padre
        print(self.mensaje) # luego imprimo el atributo que se modificara en el objeto "focasa.hablar"


marinito = Marino()
marinito.hablar()

pulpin = Pulpo ()
pulpin.hablar()

focasa= Foca()
focasa.hablar("Hola, soy una foca") #invoco el metodo hablar de la clase padre "Marino" y lo ejecuto en la clase hija "Foca" y pongo el mensaje de "Hola, soy una foca" para modificar el atributo y se muestre impreso