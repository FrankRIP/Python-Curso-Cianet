'''
Crear un programa que tenga una lista, luego crear una funcion con la cual se van a pedir numeros al usuario para agregar a la lista. Debes crear una segunda funcion en donde se ordenen los numeros pares e impares dentro de dos listas nuevas
'''

lista = []
num = 0

def pedir ():
    i = 0
    while i <= 5:                                   #mientras que i sea menor o igual a 5
        num = float (input("Ingresa un numero: "))  #aqui se pide el numero
        lista.append(num)                           #agrego un nuevo valor a la lista
        i += 1                                      #se va agregando un salto de uno en uno para no hacer infinito el ciclo

def ordenar ():
    lista.sort()                                    #sort esta ordenando de menor a mayor
    pares = []                                      #se crea la lista de pares
    impares = []                                    #se crea la lista de impares
    for i in lista:                                 #i esta en la lista
        if i % 2 == 0:                              #si el residuo de i es igual a cero
            pares.append(i)                         #entonces agrega el valor a la lista "pares"
        else:                                       #sino...
            impares.append(i)                       #agregalo a la lista "impares"
    print (pares)                                   #imprime pares
    print (impares)                                 #imprime impares

pedir()                                             #invoco la funcion pedir
ordenar()                                           #invoco la funcion ordenar