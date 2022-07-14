while True:                                     #mientras edad sea verdadero
    try:                                        #voy a intentar este programa
        edad = int (input("Ingresa tu edad:"))
        print ("Tu edad es", edad)
        break
    except:                                     #esto es para que no salga el error como tal si no que muestre un mensaje
        print("Ingresaste un valor erroneo")
    finally:
        ("La Ejecucion ha finalizado")          #este comando se ejecuta haya o no error