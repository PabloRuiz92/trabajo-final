from tkinter import *

'''
Cambiar status trabajador
En esta opción se debe buscar el trabajador por dni y cambiarle el status activo, es cuando se da
de alta/baja en un trabajo
'''

class ConsultoraStatus:
    def __init__(self):
        self.root=Tk()
        self.root.title("Consultora Estatus")
        self.root.resizable(0,0)
        #self.root.geometry("380x350")

        self.labelBienvenidaStatus = Label(self.root, text="Bienvenido, ingrese el Dni del trabajador a dar de baja/alta")
        self.labelBienvenidaStatus.grid(column=0,row=0,columnspan=4)
        
        self.botonGestion = Entry(self.root)
        self.botonGestion.grid(column=0,row=2,sticky=S+N+E+W)

        self.botonAceptar = Button(self.root, text="Aceptar")
        self.botonAceptar.grid(column=1,row=2,sticky=S+N+E+W)
        
        self.botonSalir = Button(self.root, text="Volver al menú principal", command= self.root.destroy)
        self.botonSalir.grid(column=2,row=2,sticky=S+N+E+W)

        self.root.mainloop()
            
app = ConsultoraStatus()