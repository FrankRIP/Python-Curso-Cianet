'''
Escribir un programa que, dado un número entero, muestre su valor absoluto. Nota: para los números positivos su valor absoluto es igual al número (el valor absoluto de 52 es 52), mientras que, para los negativos, su valor absoluto es el número multiplicado por -1 (el valor absoluto de -52 es 52).
'''
#abs es para sacar el valor absoluto de un numero
#ejemplo
#print (abs(5))

numero = int (input("Ingrese el numero entero: "))


if numero > 0:
    print("El valor absoluto de {} es: {}".format(numero, numero))
else:
    print("El valor absoluto de {} es: {}".format(numero, abs(numero)))