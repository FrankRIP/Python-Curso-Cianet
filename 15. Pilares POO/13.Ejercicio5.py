'''
Crear un programa con tres clases Universidad, con atributos nombre (Donde se almacena el nombre de la Universidad). Otra llamada Carerra, con los atributos especialidad (En donde me guarda la especialidad de un estudiante). Una ultima llamada Estudiante, que tenga como atributos su nombre y edad. El programa debe imprimir la especialidad, edad, nombre y universidad de dicho estudiante con un objeto llamado persona.
'''

class Universidad():
    def __init__(self, nombre):
        self.nombre = nombre
    
class Carrera ():
    def carrera (self, especialidad):
        self.especialidad = especialidad

class Estudiante (Carrera, Universidad):
    def datos (self, nombreEst, edad):
        self.nombreEst = nombreEst
        self.edad = edad
        print ("Mi nombre es {}, tengo {} años, mi especialidad es {}, y Estudio en la universidad {}.".format(self.nombreEst, self.edad, self.especialidad, self.nombre))
    
persona = Estudiante ("ITSRLL") #esto se inserta en la clase estudiante, dado que heredo el atributo de la clase universidad
persona.carrera ("Informatica") #esto se inserta en la clase estudiante, debido a que heredo el atributo de la clase carrera
persona.datos("Frank", 24)    #esto se inserta en la propia clase estudiante ya que es donde estan los atributos donde insertaran los datos