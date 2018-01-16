#Posicionamiento de ventanas en Python
from tkinter import * 

#Creacion y titulo de ventana
ventana = Tk()
ventana.title("Posicionamiento")

#Boton para cambiar el orden
boton = Button(ventana, text = 'PosicionamientoDiferente').grid(row = 0, column = 1)

#Etiqueta fila 0 columna 0
etiqueta = Label(ventana, text = 'PosicionamientoDiferente').grid(row = 0, column = 0)

#Etiqueta fila 1 columna 1
etiqueta2 = Label(ventana, text = 'PosicinamientoTablas').grid(row = 1, column = 1)

#Boton para cambiar el orden
boton2 = Button(ventana, text = 'PosicionamientoDiferente').grid(row = 2, column = 1)


ventana.mainloop()
