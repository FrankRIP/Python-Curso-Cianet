#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

edad = int (input ("Ingresa tu edad: "))

i = 1

while i < edad: #mientras "i" sea menor a la cantidad ingresada entonces...
    print ("Los años que has cumplido son, {} años.".format(i))#imprime el salto de linea de "i" que es de 1 en 1
    i += 1 #"+=" es para ir agregando una cantidad en especifico a la variable, en este caso agrego de 1 en 1