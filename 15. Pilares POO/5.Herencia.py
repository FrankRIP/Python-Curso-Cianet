class animales ():
    def habla(self):
        print ("Yo soy un animal")

    def descripcion(self):
        print ("Yo soy un {}".format(self.animal)) #se invoca el self.animal del metodo abeja

class perro (animales): #Al ponerle yo en otra clase el nombre de la clase de arriba, estoy heredando clases
    pass

class abeja (animales):
    def __init__ (self, animal):#creo el parametro animal para
        self.animal = animal

animal = animales() #creo el metodo de la clase animales
animal.habla()

perru = perro() #creo el objeto de la clase perro como como heredo todos los atributos de la clase habla lo puedo invocar aqui tambien
perru.habla()

abeju = abeja ("Abeja")#creo el objeto con la invocacion del metodo abeja
abeju.descripcion()#mando a llamar el metodo descripcion para introducirle el argumento de "Abeja"
