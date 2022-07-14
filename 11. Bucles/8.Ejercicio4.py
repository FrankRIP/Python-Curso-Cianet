'''
Pedir al usuario que ingrese 2 numeros, después, se debe mostrar el rango de esos 2 números, pero, solo imprimiendo los números que sean impares
'''

pri = int (input("Ingresa el primer numero: "))
seg = int (input("Ingresa el segundo numero: "))

for i in range (pri, seg +1):#se pone "+1" ya que no imprime el valor de la derecha
    if i % 2 == 0:  #se evalua si la divicion de "i" es igual a cero
        continue    #si es igual a cero entonces continua el ciclo
    print (i)
