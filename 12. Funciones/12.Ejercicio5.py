'''
Crear un programa que tenga dos funciones, una que contenga el area de un cuadrado con argumentos de base y altura; y la otra el area de un circulo con argumento de radio
'''

def cuadrado (base, altura):
    return base * altura

print (cuadrado(10, 10))

def circulo (radio):
    return pow(radio, 2) * 3.14

print (circulo(10))
    