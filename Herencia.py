#Ejemplo de herencia
class Electrodomestico:

    #Metodo constructor
    def __init__(self, nombre):
        self.nombre = nombre
        self.estado =False
    
    #Metodo encender electrodomestico
    def encender(self):
        if(self.estado == False):
            self.estado = True
            print('Se ha encendido:', self.nombre)
        else:
            print('El electrodomestico estaba encendido')
    
    #Metodo apagar electrodomestico
    def apagar(self):
        if(self.estado == True):
            self.estado = False
            print('Se ha apagado:', self.nombre)
        else:
            print('El electrodomestico estaba apagado')

#Clase Telefono para comprobar herencia multiple
class Telefono:
    
    def llamar(self):
        print('Llamando')
    
    def colcar(self):
        print('Llamada finalizada')

#Clase celular herencia electrodomesticos and Telefono
class Celular(Electrodomestico, Telefono):
    
    def mandarMensaje(self):
        if(self.estado == True):
            print('Mandando mensaje')

#Clase television herencia electrodomesticos
class Television(Electrodomestico):
    
    def cambiarCanal(self):
        if(self.estado == True):
            print('Cambiando de canal')



cel1 = Celular('Alcatel')
cel1.encender()
cel1.mandarMensaje()
cel1.llamar()
cel1.colcar()
cel1.apagar()
        
tel1 = Television('Television 1')
tel1.encender()
tel1.cambiarCanal()
tel1.apagar()
            
