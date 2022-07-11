lista = [1, 2, 3, 4, 5]
lista2 = [5, 3 , 1, 4, 1]
#count es para contar la cantidad de veces que se repite un valor dentro de la lista
#le digo que me cuente las veces que se repite el "5" en la lista
print (lista.count(5))

#index me dice en que espacio esta el valor que le ingreso
#por ejemplo quiero saber en que posicion esta el 4
#pero me va a decir solo donde esta la primera posicion del valor ingresado
#si hay 3 "4" solo me dira donde esta el primer "4"
print(lista.index(4))

#sort es para ordenar la lista de menor a mayor
lista2.sort()
print(lista2)

#reverse es para ordenar la lista de mayor a menor
lista2.reverse()
print(lista2)