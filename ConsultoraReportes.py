from tkinter import *

'''
Reportes
[1] Mostrar trabajadores Activos
[2] Mostrar trabajadores desocupados
[3] Mostrar desocupados en un rango de edad
[4] Mostrar trabajadores según la profesión
[0] Volver al menú principal
'''

class ConsultoraReportes:
    def __init__(self):
        self.root=Tk()
        self.root.title("Consultora Reportes")
        self.root.resizable(0,0)
        #self.root.geometry("380x350")

        self.labelBienvenidaReportes = Label(self.root, text="Bienvenido")
        self.labelBienvenidaReportes.grid(column=0,row=0,columnspan=5)
        
        self.botonTrabajadoresActivos = Button(self.root, text="Mostrar trabajadores Activos")
        self.botonTrabajadoresActivos.grid(column=0,row=2,sticky=S+N+E+W)

        self.botonTrabajadoresDesocupados = Button(self.root, text="Mostrar trabajadores desocupados")
        self.botonTrabajadoresDesocupados.grid(column=1,row=2,sticky=S+N+E+W)
        
        self.botonDesocupadosEdad = Button(self.root, text="Mostrar desocupados en un rango de edad")
        self.botonDesocupadosEdad.grid(column=2,row=2,sticky=S+N+E+W)

        self.botonProfesion = Button(self.root, text="Mostrar trabajadores según la profesión", command= self.root.destroy)
        self.botonProfesion.grid(column=3,row=2,sticky=S+N+E+W)

        self.botonVolver = Button(self.root, text="Volver al menú principal", command= self.root.destroy)
        self.botonVolver.grid(column=4,row=2,sticky=S+N+E+W)

        self.root.mainloop()
            
app = ConsultoraReportes()