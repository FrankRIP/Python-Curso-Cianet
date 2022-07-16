class A():
    def __init__(self):
        self._cuenta = 0
        self._contador = 0

    @property #al ponerle esta palabra le digo que estoy haciendo metodo get pero lo puedo mandar a llamar como atributo
    def cuenta(self):
        return self._cuenta

    @property
    def contador(self):
        return self._contador

a = A()
#print (a._cuenta) #esto se puede hacer pero es erroneo
print (a.cuenta) #asi es como se debe de llamar el atributo, si pongo property arriba, aqui le puedo quitar los parentesis