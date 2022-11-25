from tkinter import *
import pickle

'''
Gestión de Trabajadores
Deberá mostrar otro menú con estas opciones:
[1] Ingresar nuevo Trabajador
[2] Modificar dato de trabajador
[3] Eliminar Trabajador
[0] Volver al menú principal
'''
class ConsultoraGestion:
    def __init__(self):
        self.root=Tk()
        self.root.title("Consultora Gestion")
        self.root.resizable(0,0)
        #self.root.geometry("380x350")

        self.labelBienvenidaGestion = Label(self.root, text="Gestion de trabajadores")
        self.labelBienvenidaGestion.grid(column=0,row=0,columnspan=4)
        
        self.botonIngresoTrabajador = Button(self.root, text="Ingresar nuevo Trabajador")
        self.botonIngresoTrabajador.grid(column=0,row=2,sticky=S+N+E+W)

        self.botonModoficarTrabajador = Button(self.root, text="Modificar dato de trabajador")
        self.botonModoficarTrabajador.grid(column=1,row=2,sticky=S+N+E+W)
        
        self.botonEliminarTrabajador = Button(self.root, text="Eliminar Trabajador")
        self.botonEliminarTrabajador.grid(column=2,row=2,sticky=S+N+E+W)

        self.botonVolver = Button(self.root, text="Volver al menú principal", command= self.root.destroy)
        self.botonVolver.grid(column=3,row=2,sticky=S+N+E+W)

        self.root.mainloop()
            
app = ConsultoraGestion()