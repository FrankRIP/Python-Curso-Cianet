'''
Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden las tres últimas letras tiene que decir que riman. Si coinciden sólo las dos últimas tiene que decir que riman un poco y si no, que no riman.
'''

palabra1 = input("Ingresa la primer palabra: ") 
palabra2 = input("Ingresa la segunda palabra: ") 

#len es para saber cuantos espacios tiene la cadena de texto y si coinciden lo hace saber

#le pongo que si las palabras son menores a 3 letras salga el texto que quiero imprimir
if len(palabra1) < 3 or len(palabra2) < 3:
    print("No rima por que tiene menos de 3 caracteres")
#se hace debanado de cadena aqui se tomaran los 3 ultimos valores para ver si son iguales,
#puede ser [0 : 3] o como en el ejercicio [-3 : ] para indicar que quiero solo los ultimos 3 valores
elif palabra1 [-3 : ] == palabra2 [-3 : ]:
    print("Las palabras riman")
elif palabra1 [-2 : ] == palabra2 [-2 : ]:
    print("Las palabras riman un poco")
else:
    print("Las palabras no riman")