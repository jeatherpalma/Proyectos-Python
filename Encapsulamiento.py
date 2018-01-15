#Encapsulamiento
class Nacimiento:

    def __init__(self):
        self.__anio = 2000
        self.__mes = 1
        self.__dia = 1 #Dos guiones bajo se vuelven privadas las variables


    #Acceso a variables privadas get and set
    def setMes(self, mes):
        if(mes > 0 and mes < 13):
            self.__mes = mes #Accedemos con self.__ a la variable privada
        else:
            print('Valor invalido')

    def getMes(self):
        return self.__mes


nac1 = Nacimiento()
print(nac1.getMes())

#Acceder a una variable privada [objeto]._[Clase]__[variable]