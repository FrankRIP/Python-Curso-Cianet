'''
class FabricaTelefonos():
    marca ="Samsung"

    def ElaborarHuawei(self):#self permite englobar atributos a todo el programa por si lo quiero invocar en otro contexto
        self.marca = "Huawei"

telefono = FabricaTelefonos()
print (telefono.marca) #mando a llamar el atributo 

telefono.ElaborarHuawei()#mando a llamar al metodo
print (telefono.marca)
'''

class FabricaTelefonos ():
#init es para solo crear un objeto y gracias a eso puedo invocarlo en cualquier contexto
    def __init__(self, marca, color):#mando llamar al metodo init, se recomienda poner los atributos como parametros
        self.marca = marca
        self.color = color

telefono = FabricaTelefonos('Huawei', 'Negro')#creo el objeto
print (telefono.marca)
print (telefono.color)