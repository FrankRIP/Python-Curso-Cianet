while True:
    try:
        num1 = int (input("Ingresa un numero: "))
        resultado = 100 / num1
        print (resultado)
        break
    except ZeroDivisionError:#ayuda a detectar que no se puede dividir entre cero
        print ("No se puede dividir entre cero")

while True:
    try:
        edad = int(input("Ingresa tu edad: "))
        print ("Tu edad es: ", edad)
        break
    except ValueError:#ayuda a detectar si no es un cadena de texto
        print ("Has colocado un valor erroneo")

while True:
    try:
        edad = int(input("Ingresa tu edad: "))
        print ("Tu edad es: ", edad)
        break
    except KeyboardInterrupt:#si el usuario hace control+c se cancela la ejecucion del programa
        print ("\nHas cancelado la ejecucion")
        break