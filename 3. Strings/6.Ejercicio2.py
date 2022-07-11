'''
Crear un programa que tenga una variable con la cadena “Separado” y un carácter de coma (,); e inserte el carácter entre cada letra de la cadena. Ej: separar y , debería devolver s,e,p,a,r,a,r

Pista: Debes utilizar un método de las cadenas llamado “Replace”, recuerda que la posición de los caracteres empieza en 0.
'''

cade = "Separado"
cade2= "Este es el uso del metodo replace"

'''
replace es para remplazar caracteres dentro de una cadena, se invoca en metodo, y luego
se indica entre comillas que caracter va a remplazar, luego en otras comillas el caracter
por el que se va a remplazar...
En este caso fue "e" por "E"
'''
print (cade2.replace("e", "E"))

#separo por coma
print (cade.replace("" , ","))
