class A():
    def __init__(self):
        self.contador = 0
    
    def incrementar(self):
        self.contador  += 1

    def cuenta(self):
        return self.contador

class B():
    def __init__(self):
        self.__contador = 0 #cuando se agregan 2 guiones bajos, se esta encapsulando el atributo, se encapsula para poder acceder a el desde la misma clase
    
    def incrementar(self):
        self.__contador  += 1

    def cuenta(self):
        return self.__contador
 
#pyhton me dejara hacer las instrucciones que le indico pero es un error en POO, no se debe hacer 
a = A()
print (a.cuenta())#mando a llamar el metodo
a.incrementar()
print(a.cuenta)
print (a.contador)#mando a llamar el atributo

b = B()
print(b.cuenta())
b.incrementar()
print(b.cuenta)
print(b.__contador)