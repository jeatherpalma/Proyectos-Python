from tkinter import *

def imprimir():
    print("Acabas de precionar el boton imprimir")



ventana = Tk()#Creamos ventana
ventana.title("Segunda venatana")#Agregamos titulo

#fg para cambiar el color de los botones
botonSalir = Button(ventana, text="Salir", fg = "red", command = ventana.quit)#Creamos noton de salir
botonSalir.pack(side=LEFT)#Empaquetamos el boton de impirmir LADO IZQUIERDO

botonImprimir = Button(ventana, text = 'Imprimir', fg = "blue", command = imprimir)#Creamos el boton de imprimir
botonImprimir.pack(side=RIGHT)#Empaquetamos el boton lado derecho

ventana.mainloop()#Loop para ejecutar la ventana