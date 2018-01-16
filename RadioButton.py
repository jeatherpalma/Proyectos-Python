#RadioButton
from tkinter import *

def operacion():
    
    if(opcion.get() == 1):
        total = numero.get() * 10
    elif (opcion.get() == 2):
        total = numero.get() * 20
    elif (opcion.get() == 3):
        total = numero.get() * 30
    elif (opcion.get() == 4):
        total = numero.get() * 40
    elif (opcion.get() == 5):
        total = numero.get() * 50
    elif (opcion.get() == 6):
        total = numero.get() ** 2
    
    print('El total es:',total)

ventana = Tk()
ventana.title("Radiobutton en tkinter")
ventana.geometry("400x300")

#Variables para entradas
opcion = IntVar()
numero = IntVar()
#Colocando por default el radio button 1
opcion.set(1);

#Etiqueta para caja de numero
etiquetaNumero = Label(ventana, text = 'Escribe el numero:').place(x = 20, y = 30)
#Caja para caja de numero
cajaNUmero = Entry(ventana, textvariable = numero).place(x = 135, y = 30)

#Etiqueta para la opcion
etiquetaOPcion = Label(ventana, text = 'Selecciona la opcion').place(x = 20, y = 70)


#RadioButon
x10 = Radiobutton(ventana, text = 'X10', value = 1, variable = opcion).place(x = 20, y = 95)
#RadioButon
x20 = Radiobutton(ventana, text = 'X20', value = 2, variable = opcion).place(x = 70, y = 95)
#RadioButon
x30 = Radiobutton(ventana, text = 'X30', value = 3, variable = opcion).place(x = 120, y = 95)
#RadioButon
x40 = Radiobutton(ventana, text = 'X40', value = 4, variable = opcion).place(x = 20, y = 125)
#RadioButon
x50 = Radiobutton(ventana, text = 'X50', value = 5, variable = opcion).place(x = 70, y = 125)
#RadioButon
cuadrado = Radiobutton(ventana, text = 'Cuadrado', value = 6, variable = opcion).place(x = 120, y = 125)


botonOperacion = Button(ventana, text = 'Realizar operacion', command = operacion).place(x = 80, y = 180)

ventana.mainloop()