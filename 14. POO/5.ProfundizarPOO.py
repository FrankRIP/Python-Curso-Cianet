class FabricaTelefonos ():
    def __init__(self, marca, *colores, **modelos):#con * le estoy diciendo que no se cuantos valores voy a ingresar, solo que ingresare varios y de varios caracteres, puede ser * para almacenar en tuplas o ** para almacenar en diccionarios
        self.marca = marca
        self.colores = colores
        self.modelos = modelos

#se crea el objeto
telefono = FabricaTelefonos ("Alcatel", "Negro", "Azul", "Rojo", m1 = 500, m2 = 100)#asi es como reconoce python que es un diccionario
print (telefono.marca)
print (telefono.colores)
print (telefono.modelos)
#se crea un objeto temporal que se atribuye al objeto
telefono.memoria = 512
print (telefono.memoria)