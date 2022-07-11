'''
En el siguiente diccionario se encuentran capitales de los paises en el mundo, debes realizar un programa que pida un pais al usuario, y muestre la capital de ese pais, en dado caso el pais no este en el diccionario, se debe mostrar un mensaje diciendo que ese pais no se encuentra.

{"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}
'''

diccionario = {"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Tegucigalpa","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}

pais = input("Ingrese un pais  para conocer su capital: ")

#capitalize es  para convertir una letra miniscula en mayuscula, pero sera solo la primer letra
#in es para asegurarnos que un elemento este adentro de otro
letra = pais.title() in diccionario

if letra == True:
    print(diccionario[pais.title()])#mando a llamar pais que es la clave del diccionario y me imprimira el valor que es la capital
else:
    print("El pais no se encuentra en el diccionario")

'''
Otra forma de hacerlo seria

if pais.capitalize() in diccionario:
    print (diccionario[pais.capitalize()])
else:
    print("El pais no se encuentra en el diccionario")
'''