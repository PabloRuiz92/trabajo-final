from tkinter import *

class ConsultoraReportes:
    def __init__(self):
        self.root=Tk()
        self.root.title("Consultora Reportes")
        self.root.resizable(0,0)
        #self.root.geometry("380x350")

        self.labelBienvenida = Label(self.root, text="Bienvenido")
        self.labelBienvenida.grid(column=0,row=0,columnspan=4)
        
        self.botonGestion = Button(self.root, text="Gestion de trabajadores")
        self.botonGestion.grid(column=0,row=2,sticky=S+N+E+W)

        self.botonReportes = Button(self.root, text="Reportes")
        self.botonReportes.grid(column=1,row=2,sticky=S+N+E+W)
        
        self.botonStatus = Button(self.root, text="Cambiar status trabajador")
        self.botonStatus.grid(column=2,row=2,sticky=S+N+E+W)

        self.botonSalir = Button(self.root, text="Salir", command= self.root.destroy)
        self.botonSalir.grid(column=3,row=2,sticky=S+N+E+W)

        self.root.mainloop()
            
app = ConsultoraReportes()