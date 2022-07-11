#un condicional anidado, es una condicional que esta dentro de otra condicional

nombre = "Juan"
edad = 18

#if y else deben siempre ir alineados
if nombre == "Juan":
    if edad >= 18:
        print ("Eres Juan y tienes mayoria de edad")
    else:
        print ("Eres Juan, pero no tienes mayoria de edad")
else:
    print ("Tu no eres Juan")
