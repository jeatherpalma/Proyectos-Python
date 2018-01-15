#Ejemplo de clase en python
class Gelatina:

    #Metodo tipo constructor pasando self
    def __init__(self, tam, color, sabor):
        self.tam = tam
        self.color = color
        self.sabor = sabor

    #Metodo que desplega un documento
    def desplegarCaracteristicas(self):
        print(self.tam, self.color, self.sabor)
        


#Creacion de los objetos
gel1 = Gelatina('Chica', 'Rojo', 'Fresa')
gel2 = Gelatina('Mediana', 'Amarilla', 'Mango')
gel3 = Gelatina('Grande', 'Azul', 'Moras')


gel1.desplegarCaracteristicas()
gel2.desplegarCaracteristicas()
gel3.desplegarCaracteristicas()