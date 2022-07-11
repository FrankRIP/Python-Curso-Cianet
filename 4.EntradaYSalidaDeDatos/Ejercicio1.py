'''
Ejercicio 1

Realizar un programa que haga el proceso de formula general para la resolución de ecuaciones, sabiendo que la formula general es la que está en la imagen, el usuario debe ingresar los valores de “a”, “b” y “c”, y el programa debe hacer el proceso para que al final muestre el mensaje: “La solución es: <solucion>”
'''

#importo libreria
#sqrt es equivalente a una funcion de raiz cuadrada
from math import sqrt

#ejemplo
print ("Este es el ejemplo de lo que hace sqrt:", sqrt (100))#sqrt va a sacar la raiz cuadrada de 100

a = int (input("Ingresa el valor A: "))
b = int (input("Ingresa el valor B: "))
c = int (input("Ingresa el valor C: "))
x1 = 0
x2 = 0

if ((b**2)-(4*a*c)) <0:
    print ("No se puede realizar por que no se puede sacar raiz a un numero negativo")
else:
    x1 = (-b + sqrt ((b**2) - (4*a*c))) / (2*a)
    x2 = (-b - sqrt ((b**2) - (4*a*c))) / (2*a)

print ("La solucion es: \nx1=", x1, "\nx2= ", x2)