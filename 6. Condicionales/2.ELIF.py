letra = "E"

#cuando se trata de caracteres siempre se debe de poner entre comillas
if letra == "a":
    print ("Esta vocal es la A")
#elif es para poner muchas condiciones y no se cierra el ciclo com si pusiera else
elif letra.lower() == "e":
    print ("Esta vocal es la E")
elif letra.lower() == "i":
    print ("Esta vocal es la I")
elif letra.lower() == "o":
    print ("Esta vocal es la O")
#si ninguna de las condiciones anteriores se cumplen, entonces se cierra ciclo con else
else:
    print ("Esta vocal es la U")
