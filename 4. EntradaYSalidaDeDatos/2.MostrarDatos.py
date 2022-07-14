nombre = input("Ingresa tu nombre: ")
edad = int (input("Ingresa tu edad: " ))

'''
format es para concatenar variables en el print, en las primeras llaves se va a imprimir automaticamente
el primer valor que es "nombre" y en las segundad llaves se va a imprimir el segundo valor que es "edad"
y de la siguiente manera es como se invoca y ejecuta el metodo "format"
'''
print("Hola {} tienes {} años".format(nombre, edad))