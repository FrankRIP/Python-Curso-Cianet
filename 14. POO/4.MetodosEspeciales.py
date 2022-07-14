from email.errors import MalformedHeaderDefect
from turtle import color


class FabricaTelefonos ():
    def __init__(self, marca, color) :#se inicia el metodo constructor
        self.marca = marca
        self.color = color
        print ("El objeto {} ha sido creado".format(self.marca))

    def __str__(self):#esto es para darle un mensaje descriptivo y no salgan cifras extrañas en la terminal
        return "El objeto es {}".format(self.marca)

    def __del__(self): #se ejecuta el metodo destructor
        print ("El objeto {} ha sido destruido".format(self.marca))

telefono = FabricaTelefonos("Nokia", "Negro")#se crea un objeto
print (telefono.marca)
print (telefono)