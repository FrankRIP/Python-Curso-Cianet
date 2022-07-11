#las listas son mutables (o sea que se pueden cambiar sus valores)
#Listas homogeneas: Que son del mismo tipo de datos
#heterogeneas: Que son de diferente tipo de datos
#(String, float, int, bool, etc.)

#Estructura de una lista
lista = ['Python', 120, 'Nombre', 4.14, 6.28]
print (type(lista))

#Asi es como mando llamar un espacio especifico de la lista
#imprimo la lista y entre los corchetes el espacio que mande a llamar
print (lista[3])

#len tambien ayuda para saber cual es el tamaño de la lista
print(len(lista))

#Asi es como se cambia un valor de la lista
#Entre los corchetes le digo cual espacio quiero cambiar y en las comillas
#como es que lo quiero cambiar, estaba "Python" y lo cambie a "python"
lista [0] = "python"
print(lista)