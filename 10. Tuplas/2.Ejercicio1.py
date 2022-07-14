'''
Escribir una tupla con los meses del año, luego, pide al usuario un numero, el que haya ingresado, es el mes que debe mostrar en la tupla

'''

'''
Teniendo en cuenta que los espacion en las tuplas y listas comienzan desde la posicion "0"
se le va a restar "-1" al numero que haya ingresado el usuario para asi poder coincidir con
el numero ingresado por el usuario
'''

tupla = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre",
 "Noviembre", "Diciembre")

mes = int (input ("Elija un numero (Del 1 al 12): "))

print ('El mes que elejiste fue: "{}"'.format(tupla[mes -1])) #Aqui se resta el uno para conincidir con la posicion del numero que ingreso el usuario.