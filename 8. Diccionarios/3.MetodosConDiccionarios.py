diccionario = {1: 2, 2: 3, 3: 4}
diccionario2 = {4: 5, 6: 7}

#pop en las listas elimina solo el ultimo valor
#pero en diccionario le doy la clave que quiero eliminar y elimina la clave y valor
diccionario.pop(3)
print(diccionario)

#clear es para limpiar todo el diccionario
diccionario.clear()
print (diccionario)

#get es para decirle que nos la clave del espacio que le indicamos
print (diccionario.get(2))

#setdefault es para ingresar un nuevo valor al final del diccionario
#le digo que ingresare una llave "4" y su valor que es "5"
diccionario.setdefault(4 , 5)
print (diccionario)

#update es para actualuzar un diccionario, aqui le digo que me actualice ingresando los valores
#de diccionario 2 en el primero
diccionario.update(diccionario2)
print(diccionario)

#copy es para crear una copia del diccionario
diccionario.copy()
print(diccionario)