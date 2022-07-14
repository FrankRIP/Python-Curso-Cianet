def valores ():
    global num1 #estoy haciendo global esta variable y puedo invocarla en otros contextos, luego la invoco en este mismo contexto pero ya con un valor
    global num2 
    num1 = 110
    num2 = 40
    resultado = num1 + num2
    return resultado

print (valores())

resta = num1 - num2
print (resta)