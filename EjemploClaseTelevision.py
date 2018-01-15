class Television:

    def __init__(self, marca):
        self.marca = marca
        self.encendida = False

    def prender(self):
        if(self.encendida == False):
            self.encendida = True
        else:
            print('La television esta prendida')

    
    def apagar(self):
        if(self.encendida == True):
            self.encendida = False
        else:
            print('La television esta apagada')


    def saberMarca(self):
        print('Esta es la marca: ', self.marca)



tel1 = Television('Samsung')
tel1.prender()
tel1.prender()
tel1.apagar()
tel1.apagar()
tel1.saberMarca()