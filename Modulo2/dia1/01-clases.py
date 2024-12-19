class Automovil:
    #Creamos el metodo constructor
    def __init__(self,aa,pl,col,mar):
        self.año = aa
        self.placa = pl
        self.color = col
        self.marca = mar
    
    #Metodos
    def encender(self):
        print("encender" + self.marca)

    def avanzar(self):
        print("avanzar" + self.marca)

    def acelerar(self):
        print("acelerar" + self.marca)

    def frenar(self):
        print("frenar" + self.marca)

##Creamos Objetos
vw = Automovil(1970, "CH-1234","Amarillo","Volkswagen")
vw.encender()
vw.acelerar()
vw.frenar()
print("==================")

tico = Automovil(1985, "EJ-2345","Rojo","Daewoo")
tico.encender()
tico.acelerar()
tico.frenar()
print("==================")

aventador = Automovil(2010, "EX-2500","Negro","Lamborghini")
aventador.encender()
aventador.acelerar()
aventador.frenar()
print("==================")