'''
Crear un programa que pida al usuario una letra, y si es vocal, muestre el mensaje "Es vocal". Sino, decirle al usuario que no es vocal
'''

vocal = input ("Ingresa una letra: ")

'''
#el metodo lower convierte las mayusculas a minusculas en caso de que el usuario ponga las letras en mayusculas
if vocal.lower() == "a":
    print ("Es una vocal")
else:
    if vocal.lower()  == "e":
        print ("Es una vocal")
    else:
        if vocal.lower()== "i":
            print ("Es una vocal")
        else:
            if vocal.lower()== "o":
                print ("Es una vocal")
            else:
                if vocal.lower() == "u":
                    print ("Es una vocal")
                else:
                    print("No es una vocal")
'''

#la otra forma de hacerlo seria...

if vocal.lower() in "aeiou":
    print("Es una vocal")
else:
    print("No es una vocal")