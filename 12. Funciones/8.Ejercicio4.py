'''
Escribir una función que calcule el total de una factura tras aplicarle el IVA. 
La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar,
y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, 
deberá aplicar un 21%.
'''
def aplicarIva ():
    cant = float (input ("Indique la cantidad a aplicar de Iva: "))
    iva = float (input ("Indique el IVA que va a aplicar: "))
    if iva != 0:        # conector1. si el iva es diferente de 0 o sea que no le indico cantidad
        if iva > 0:                                 #si el iva es mayor a 0 o sea que si le indique algun motno
            totalPago = ((cant * iva) / 100) + cant #entonces agregalo a la cantidad que le ingrese
            return totalPago                        #y regresame el valor total del producto ya con iva
        else:
            return "El monto de IVA es negativo, no se puede hacer la operacion"
    else:               #conector1. entonces automaticamente se sacara el 21% y se suma a la cantidad del producto
        aplicarPago = (cant * 0.21) + cant
        return totalPago

print ("El total del costo es (Ya con IVA aplicado): ",aplicarIva())
