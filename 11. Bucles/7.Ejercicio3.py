'''
Imprimir por pantalla los numeros del 1 al 10, luego, pedir al usuario dos numeros y mostrar el rango de numeros entre ambas cifras
'''
for i in range (1, 11):
    print (i)

numerouno = int (input("Ingresa el primer numero: "))
numerodos = int (input("Ingresa el segundo numero: "))

for i in range (numerouno, numerodos +1): #se pone "+1" ya que no imprime el valor de la derecha
    print (i)