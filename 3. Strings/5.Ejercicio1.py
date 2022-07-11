'''
Crear un programa, que tenga una variable con la cadena “Te quiero solo como amigo”, y muestre la siguiente información:

• Imprima los dos primeros caracteres.

• Imprima los tres últimos caracteres.

• Imprima dicha cadena cada dos caracteres. Ej.: Si la cadena fuera “recta” debería imprimir rca

• Dicha cadena en sentido inverso. Ej.: Si la cadena fuera hola mundo! debe imprimir !odnum aloh

• Imprima la cadena en un sentido y en sentido inverso. Ej: Si la cadena es “reflejo” imprime reflejoojelfer.
'''

frase = "Te quiero solo como amigo"

print (len(frase))

#Imprimo solo los 2 primeros caracteres
print (frase [0 : 2])

#Imprimo solo los ultimos 3 caracteres
print (frase [-3 : ])

'''
La sintaxis es que con los primeros dos puntos le ordenamos que saque una copia de la cadena, los
segundos dos puntos son para indicar la operacion.

2 es para imprimir de 2 en 2 y -1 es para imprimir la cadena a la inversa
'''
#Imprimo cada dos caracteres
print (frase[: : 2])

#imprimo la cadena a la inversa
print(frase[: : -1])

#imprimo en sentido normal y luego inverso
print(frase, frase [: : -1])