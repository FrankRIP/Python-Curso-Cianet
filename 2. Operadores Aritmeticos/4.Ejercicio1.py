'''
Hacer la operacion de 
(3+2/2.5)^2

*El resultado debe ser 4*
'''
num1 = 3
num2 = 2
num3 = 5

print (((num1 + num2) / (num2 * num3)) ** num2)

#O bien puede ser...
print (((3 + 2) / (2 * 5)) ** 2)

#Tambien con la funcion pow

'''
pow sirve para elevar numeros, toma el primero valor y lo eleva por el segundo

ejemplo
pow (5 , 2)

pow hace que se tome el primer valor que es 5 y lo eleva por el segundo que es 2
'''
operacion = pow (((3 + 2 ) / (5 * 2)) , 2)
print (operacion)