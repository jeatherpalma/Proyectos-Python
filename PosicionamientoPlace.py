#Posicionamiento de ventanas en Python con place
from tkinter import * 

#Creacion y titulo de ventana
ventana = Tk()
ventana.title("Posicionamiento")#Titulo de la ventana
ventana.geometry("400x200")#Tamaño de la ventana


def saludar():
    print("Hola a todos")

def minimizar():
    ventana.iconify()


#Boton para cambiar el orden
boton = Button(ventana, text = 'Desde aqui saludamos', command = saludar).place(x = 200, y = 10)#Place cordenadas x and y

#Etiqueta fila 0 columna 0
etiqueta = Label(ventana, text = 'Desde aqui saludamos').place(x = 10, y = 10 )#Place cordenadas x and y

#Etiqueta fila 1 columna 1
etiqueta2 = Label(ventana, text = 'Desde aqui minimizamos').place(x = 10, y = 50)#Place cordenadas x and y

#Boton para cambiar el orden
boton2 = Button(ventana, text = 'Desde aqui minimizamos', command = minimizar).place(x = 200, y = 50)#Place cordenadas x and y


ventana.mainloop()
