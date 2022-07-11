diccionario = {'Nombre': "Frank", 'Apellido': "Moran", "Estatura": 1.82}

print (diccionario)

#keys es para mostrar solo las claves del diccionario
print (diccionario.keys())

#values es para mostrar solo los valores del diccionario
print (diccionario.values())

#Estructura para ver valores en especifico de una clave del diccionario
#imprimo el diccionario y entre corchetes el valor del diccionario que quiero en especificio
print(diccionario["Estatura"])

#Estructura para agregar un nuevo elemento al diccionario
#invoco el diccionario como variable y entre corchetes la nueva clave y luego el valor
diccionario ["Peso"] = "74 kg"
print (diccionario)

diccionario ["Nombre"] = "Franksito"
print (diccionario)