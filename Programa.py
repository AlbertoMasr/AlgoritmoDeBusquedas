from tkinter import *
from Busquedas import AAsterisco, Amplitud, PrimeroElMejor, Profundidad
from Nodos import *

class Programa(object):
    
    def __init__(self):
        self.ventana = Tk()
        # Pantalla principal
        self.ventana.title("Algoritmos de búsquedas")
        self.ventana.geometry("600x600")
        self.frame = Frame(self.ventana)
        self.frame.pack(side=TOP)
        # Menú
        (Label(self.frame, text="Seleccione un juego").grid(row=1, column=1, columnspan=2))
        Button(self.frame, text="Camino", width=15, height=1, command=lambda: self.opcion(1)).grid(row=2, column=1)
        Button(self.frame, text="Conecta 3", width=15, height=1, command=lambda: self.opcion(2)).grid(row=2, column=2)
        self.menu = Frame(self.ventana)
        self.menu.pack(side=LEFT)
        # Tipos de búsqueda
        Label(self.menu, text="Seleccione una búsqueda").pack()
        Button(self.menu, text="Profundidad", width=15, height=1, command=lambda: self.opcion(3)).pack()
        Button(self.menu, text="Amplitud", width=15, height=1, command=lambda: self.opcion(4)).pack()
        Button(self.menu, text="A*", width=15, height=1, command=lambda: self.opcion(5)).pack()
        Button(self.menu, text="Primero el mejor", width=15, height=1, command=lambda: self.opcion(6)).pack()
        self.opciones = Frame(self.ventana)
        self.opciones.pack(side=RIGHT)
        # Muestra la pantalla principal
        self.imput = None
        self.inicial = None
        self.seleccion = None
        self.ventana.mainloop()

    def opcion(self, opc):
        if opc == 1:
            self.inicial = None
            self.seleccion = 1
            self.inicial = NodoCamino(None, [], None)
            self.opciones.destroy()
            self.opciones = self.inicial.crear_estado_inicial(self.ventana)
            self.opciones.pack(side=RIGHT)
        elif (opc > 2 and (self.seleccion == 1 and 'M' in self.inicial.estado and 'R' in self.inicial.estado)):
            print("Entró")
            if opc == 3:
                busqueda = Profundidad(self.inicial)
            elif opc == 4:
                busqueda = Amplitud(self.inicial)
            elif opc == 5:
                busqueda = AAsterisco(self.inicial)
            elif opc == 6:
                busqueda = PrimeroElMejor(self.inicial)
            busqueda.cronometro(busqueda.buscar)
            self.opciones.destroy()
            self.opciones = busqueda.crear_frame(self.ventana)
            self.frame.pack(side=RIGHT)

# Ejecuta el programa
if __name__ == "__main__":
    programa = Programa()