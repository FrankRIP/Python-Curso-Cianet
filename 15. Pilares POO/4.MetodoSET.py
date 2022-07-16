class A():
    def __init__(self):
        self._cuenta = 0
        self._contador = 0

    @property #al ponerle esta palabra le digo que estoy haciendo metodo get pero lo puedo mandar a llamar como atributo
    def cuenta(self):
        return self._cuenta

    @cuenta.setter #sintaxis para indicarle a python que sera un metodo "set" el cual me permitira modificar el atributo en el objeto
    def cuenta(self, cuenta):
        self._cuenta = cuenta #cuenta sera el valor que sera modificado en un futuro, aun que este el nombre en otros metodos no va a generar problemas

    @property
    def contador(self):
        return self._contador

    @contador.setter
    def contador (self, contador):
        self._contador = contador

  

a = A()#creo el objeto
print (a.cuenta)#mando a llamar al metodo "get"
a.cuenta = 20 #mando a llamar al metodo "set" para cambiarle el valor
print (a.cuenta)

print (a.contador)
a.contador = 10
print (a.contador)