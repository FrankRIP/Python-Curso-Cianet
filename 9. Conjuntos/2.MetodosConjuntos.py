conjunto = {1, 1, 2, 3, 3, 4, 4, 5}#Los conjuntos al momento de imprimir solo me mostrara una ves los datos aun que se repitan

conjunto2 = {1, 2, 3, 4, 5}

#add es para agregar un elemento al conjunto, pero lo agrega al final
conjunto2.add(20)
print (conjunto2)

#remove elimina el elemento que le indico
conjunto2.remove(1)
print (conjunto2)

#discard es para eliminar un elemento que le indico
conjunto2.discard(2)
print (conjunto2)

#update es para agregar elementos al conjunto
conjunto.update([1, 2, 3])#debe ser un elemento iterable
print (conjunto2)

#clear es para limpiar el conjunto
conjunto2.clear()
print (conjunto2)