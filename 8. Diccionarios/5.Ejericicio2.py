'''
Con el siguiente diccionario, debes crear un programa que pregunte al usuario por un número; el programa debe imprimir el jugador al que hace referencia ese número

{

    1 : "Casillas", 15 : "Ramos",

    3 : "Pique", 5 : "Puyol",

    11 : "Capdevila", 14 : "Xabi Alonso",

    16 : "Busquets", 8 : "Xavi Hernandez",

    18 : "Pedrito", 6 : "Iniesta",

    7 : "Villa"

}

'''

diccionario = {

    1 : "Casillas", 15 : "Ramos",

    3 : "Pique", 5 : "Puyol",

    11 : "Capdevila", 14 : "Xabi Alonso",

    16 : "Busquets", 8 : "Xavi Hernandez",

    18 : "Pedrito", 6 : "Iniesta",

    7 : "Villa"

}
num = int (input("Elije un numero del equipo: "))

numero = num in diccionario #indico si "num" esta en el "diccionario"

if numero == True: #si numero es igual a verdadero (o sea un numero que corresponda a las claves del diccionario)
    print((diccionario[num])) #imprimo la el valor de la clave del diccionario
else:#y si no
    print ("El jugador no existe en el equipo.")#imprimo este texto