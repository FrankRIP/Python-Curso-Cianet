#Escribir un programa que pida un numero al usuario y muestre las tablas de multiplicar de ese numero

from re import I


num = int (input('Ingresa un numero: '))
i = 0
multi = 0

while i <= 10:
    multi = num * i
    print ("{} x {} = {}".format(num, i , multi))
    i += 1 #este es el salto que va a ir dando que es de 1 en 1