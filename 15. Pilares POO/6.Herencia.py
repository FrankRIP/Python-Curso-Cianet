class animales ():
    def __init__(self, nombre):
        self.nombre = nombre

class perro (animales):
    def __init__(self, nombre, sonido):
        super().__init__(nombre) #super es para poder imprimir atributos en los objetos, asi como va la linea asi es la sintaxis
        self.sonido = sonido

perru = perro ("Firualis", "¡Guau!")
print (perru.nombre)
print (perru.sonido)