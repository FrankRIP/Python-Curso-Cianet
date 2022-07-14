class FabricaTelefonos():#Clase
    marca = "Huawei"#Atributos
    color = "Negro"
    memoriaRam = 32
    almacenamiento = 128

    def llamar(self, mensaje): #metodo (metodo de instancia)
        return mensaje

    def escucharMusica(self):
        print ("Estas escuchando musica")

telefono = FabricaTelefonos()#objeto
telefono.marca
telefono.color
telefono.memoriaRam
telefono.almacenamiento

print (telefono.almacenamiento)

print (telefono.llamar("Hola, ¿Con quien hablo?"))#se ejecuta el metodo (lo mando a llamar en este objeto)
telefono.escucharMusica()