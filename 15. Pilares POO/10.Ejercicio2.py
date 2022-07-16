'''
Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__. Calcular después la suma, resta, multiplicación y división. Utilizar un método para cada una e imprimir los resultados obtenidos. Llamar a la clase Calculadora.
'''

class Calculadora ():
    def __init__(self):
        self.numero1 = int (input("Ingrese el primer valor: "))
        self.numero2 = int (input("Ingrese el segundo valor: "))

    def suma(self):
        self.suma = self.numero1 + self.numero2
        print ("La suma es: ", self.suma)

    def resta(self):
        self.resta = self.numero1 - self.numero2
        print ("La resta es: ", self.resta)

    def multiplicacion(self):
        self.multiplicacion = self.numero1 * self.numero2
        print ("La multiplicacion es: ", self.multiplicacion)

    def division(self):
        self.division = self.numero1 / self.numero2
        print ("La division es: ", self.division)
    
resulta = Calculadora()
resulta.suma()
resulta.resta()
resulta.multiplicacion()
resulta.division()
