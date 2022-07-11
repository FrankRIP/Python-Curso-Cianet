'''
Las barras invertidas le indican a la cadena string que no se cierra en las comillas.
Si pongo la funcion asi...
cadena = "Esto es un "ejemplo" de cadena de texto"
en "ejemplo" me va a marcar error por que python piensa que se acaba la cadena en las comillas,
pero si lo pongo con diagonal invertida me leera el texto que ingrese como se hace a continuacion
'''
cadena = "Esto es un \"ejemplo\" de cadena de texto"
print (cadena)


#Tambien se aplica con comillas simples
cadena1 = 'Esto es otro \'ejemplo\' de cadena de texto'
print (cadena1)

#Salto de linea con \n
cad = "Ejemplo de cadena de texto \n con salto de linea"
print (cad)

#Tabulacion con \t
tabu = "Un ejemplo de cadena de texto \t con tabulacion"
print (tabu)