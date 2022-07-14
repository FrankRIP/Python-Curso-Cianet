'''
Escribir una tupla que tenga las letras del alfabeto. Luego, debes pedir al usuario un número, el que haya ingresado, es la letra que debe imprimir el programa
'''

'''
Teniendo en cuenta que los espacion en las tuplas y listas comienzan desde la posicion "0"
se le va a restar "-1" al numero que haya ingresado el usuario para asi poder coincidir con
el numero ingresado por el usuario
'''

tupla = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
"T", "U", "V", "W", "X", "Y", "Z")

letra = int (input("Ingresa un numero (De 1 a 26): "))
print ('La letra correspondiente al numero que elejiste es "{}"'.format(tupla[letra -1])) #Aqui se resta el uno para conincidir con la posicion del numero que ingreso el usuario.