import os

#Declaramos el nodo
class Nodo:

    def __init__(self):
        self.nombre = None
        self.edad = 0
        self.atras = None

#Clase de la pila
class Pila:

    def __init__(self):
        self.tope = Nodo()

    #Metodo de agregar(PUSH)
    def insertar(self, nodo):
        if(self.tope.nombre == None):
            self.tope = nodo
        else:
            nodo.atras = self.tope
            self.tope = nodo
    
    #Metodo de eliminar(POP)
    def eliminar(self):
        aux = self.tope
        if(aux.nombre == None):
            print('La pila esta vacia')
        else:
            self.tope = aux.atras
            if(aux.atras == None):
                self.tope = Nodo()


    #Metodo de consultar todos los datos
    def consultar(self):
        aux = self.tope
        if(aux.nombre == None):
            print('La pila esta vacia')
            
        else:
            while (aux != None):
                print('**************')
                print('Nombre: ', aux.nombre)
                print('Edada: ', aux.edad)
                aux = aux.atras
        input()
        

class Principal:
    pila = Pila()
    while True:
        os.system('clear')
        print('*******Menu*******')
        print('1.- Insertar')
        print('2.- Eliminar')
        print('3.- Consultar')
        print('4.- Salir')

        opcion = int(input('Selecciona tu opcion\n'))
        if(opcion == 1):
            nodo = Nodo()
            nodo.nombre = input('Escribe tu nombre:\n')
            nodo.edad = int(input('Escirbe tu edad:\n'))
            pila.insertar(nodo)
        elif (opcion == 2):
            pila.eliminar()
        elif (opcion == 3):
            pila.consultar()
        else:
            break
            
            