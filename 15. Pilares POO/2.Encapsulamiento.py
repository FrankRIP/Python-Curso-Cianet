class A():
    def __init__(self):
        self._contador = 0 #tambien se pone solo un guion para encapsular el atributo
        self._cuenta = 0   #todos los atributos deben ir encapsulados
    
    def incrementar (self):
        self._contador  += 1

    def cuenta (self):
        return self._contador

#pyhton me dejara hacer las instrucciones que le indico pero es un error en POO, no se debe hacer 
a = A()
#print(a.cuenta)
#a.cuenta = 20
#print (a.cuenta)

