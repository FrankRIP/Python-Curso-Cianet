'''
Escribir un programa que solicite al usuario un vocal en minuscula, y luego una letra en mayúsculas. El programa debe convertir la letra en minúscula y la vocal en mayúscula, y al final, deben ser concatenadas ambas
'''

vocal = input ("Ingresa una vocal(En minuscula): ")
letra = input ("Ingresa una consonante (En mayuscula): ")

vocal = vocal.upper()
letra = letra.lower()

print ("La vocal fue: {}\nYa la consonante fue: {}".format(vocal, letra))