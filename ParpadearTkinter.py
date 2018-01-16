from tkinter import * #Importamos tkinter
import time #Para realizar el parpadear

#Metodo que realiza el parpadeo de la ventana
def parpadear():
    ventana.iconify()
    time.sleep(1)
    ventana.deiconify()


ventana = Tk()#Creacion de la ventaba principal
ventana.title("Priemara ventana")#Agregado de titulo a la ventana

boton = Button(ventana, text="Evento", command = parpadear)#Creacion de boton
boton.pack()#Empaquetado del boton en la ventana

ventana.mainloop()#Ciclo que activa la venatan y permite que no se cierre
