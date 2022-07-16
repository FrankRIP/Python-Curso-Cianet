'''
Realizar un programa que conste de una clase llamada Estudiante, que tenga como atributos el nombre y la nota del alumno. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.
'''

class Estudiante ():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir (self):
        print ("Nombre: {}\nNota: {}".format(self.nombre, self.nota))

    def resultados (self):
        if self.nota < 7:
            print ("Has reprobado")
        else:
            print ("Has aprobado")

estudiante1 = Estudiante("Daniel", 10)#invoco al metodo de nombre y nota para agregarle los argumentos
estudiante1.imprimir()#luego los mando a insertar en el metodo imprimir
estudiante1.resultados()#y al final ejecuto el metodo resultados para ver si aprobo o no

estudiante2 = Estudiante("Karla", 5)
estudiante2.imprimir()
estudiante2.resultados()