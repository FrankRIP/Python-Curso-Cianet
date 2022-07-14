'''
Crear una funcion que pida dos numeros. Si el primero es mayor al segundo, el programa debe retornar el valor 1; si el segundo es mayor al primero, debe retornar -1; si ambos son iguales, debe retornar 0
'''

def pedir ():
    may = float (input ("Ingresa un primer numero: "))
    men = float (input ("Ingresa un segundo numero: "))
    if may > men:
        return 1
    elif may < men:
        return -1
    else:
        return 0

print (pedir())
        