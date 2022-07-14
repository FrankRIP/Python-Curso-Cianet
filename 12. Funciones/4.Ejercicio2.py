#Escribir una función que reciba un número entero positivo y devuelva su factorial.

#ejemplo de factorial =
#5 factorial es: 5*4*3*2*1

'''
def factorial ():
    num = int (input ("Ingresa un numero entero y positivo: "))
    if num > 0:
        factorial1 = 1
        for i in range (1, num +1):
            factorial1 = factorial1 * i 
        print (factorial1)
    else:
        print ("El numero es negativo y no podemos proceder")

factorial()

'''
#otra forma de hacerlo seria
def factorial ():
    from math import factorial
    num = int (input ("Ingresa un numero entero y positivo: "))
    if num > 0:
       print (factorial(num))
    else:
        print ("El numero es negativo y no podemos proceder")

factorial()