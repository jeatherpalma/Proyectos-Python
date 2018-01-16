#Entradas
from tkinter import *

def saludar():
    print("Hola", nombre.get(), apellidoP.get(), apellidoM.get())


#Creacion de ventanas
ventana = Tk()
ventana.title('Entradas')
ventana.geometry("400x400")

#Variables de Tkinter
nombre = StringVar()
apellidoP = StringVar()
apellidoM = StringVar()


#Etiueta de nombre
etiquetaNombre = Label(ventana, text = 'Escribe tu nombre: ').place(x = 10, y = 10)
#Input de nombre
nombreCaja = Entry(ventana, textvariable = nombre).place(x = 190, y = 10)#textvariable para enlazar variables tkineter
#Etiueta de apellido paterno
etiquetaApellidoP = Label(ventana, text = 'Escribe tu apellido paterno: ').place(x = 10, y = 40)
#Input de apellido paterno
apellidoPCaja = Entry(ventana, textvariable = apellidoP).place(x = 190, y = 40)
#Etiueta de apellido materno
etiquetaApellidoM = Label(ventana, text = 'Escribe tu apellido materno: ').place(x = 10, y = 70)
#Input de apellido paterno
apellidoMCaja = Entry(ventana, textvariable = apellidoM).place(x = 190, y = 70)

botonSaludar = Button(ventana, text = 'Saludo personalizado', command = saludar).place(x = 10, y = 100)


ventana.mainloop()