import copy
from tkinter import *

class Nodo(object):
    def __init__(self, padre, estado):
        self.padre = padre
        self.estado = estado
        if self.padre is None:
            self.profundidad = 0
        else:
            self.profundidad = padre.profundidad + 1

    def test_objetivo(self):
        pass

    def crear_sucesores(self):
        pass

    def calcular_costo(self):
        pass

    def calcular_heuristica(self):
        pass

    def calcular_f(self):
        self.calcular_costo()
        self.calcular_heuristica()
        self.f = self.costo + self.heuristica

    def crear_frame(self, contenedor):
        pass

class NodoCamino(Nodo):
    def __init__(self, padre, estado, operador):
        super().__init__(padre, estado)
        self.operador = operador

    def test_objetivos(self):
        if 'M' in self.estado:
            return False
        else:
            return True

    def crear_sucesores(self):
        posicion = None
        sucesores = []
        
        if self.profundidad == 0:
            posicion = self.estado.index('R')
        else:
            posicion = self.estado.index('X')
        # Moverse hacia arriba
        if posicion - 10 >= 0 and (self.estado[posicion - 10] in [0, 'M']):
            estadoaux = copy.deepcopy(self.estado)
            estadoaux[posicion - 10] = 'X'
            if(self.estado[posicion]) != 'R':
                estadoaux[posicion] = 2
            nodoaux = NodoCamino(self, estadoaux, 0)
            sucesores.append(nodoaux)
        # Moverse hacia la derecha
        if((posicion + 1) % 10) != 0 and (self.estado[posicion + 1]) in [0, 'M']:
            estadoaux = copy.deepcopy(self.estado)
            estadoaux[posicion + 1] = 'X'
            if(self.estado[posicion + 1]) != 'R':
                estadoaux[posicion] = 2
            nodoaux = NodoCamino(self, estadoaux, 1)
            sucesores.append(nodoaux)
        # Moverse hacia abajo
        if posicion + 10 <= 99 and (self.estado[posicion + 10] in [0, 'M']):
            estadoaux = copy.deepcopy(self.estado)
            estadoaux[posicion + 10] = 'X'
            if(self.estado[posicion]) != 'R':
                estadoaux[posicion] = 2
            nodoaux = NodoCamino(self, estadoaux, 2)
            sucesores.append(nodoaux)
        # Moverse a la izquierda
        if((posicion - 1) % 10) != 9 and (self.estado[posicion - 1] in [0, 'M']):
            estadoaux = copy.deepcopy(self.estado)
            estadoaux[posicion - 1] = 'X'
            if(self.estado[posicion]) != 'R':
                estadoaux[posicion] = 2
            nodoaux = NodoCamino(self, estadoaux, 3)
            sucesores.append(nodoaux)

    def calcular_cost(self):
        if self.padre is None:
            self.costo = 0
        elif self.operador == self.padre.operador:
            self.costo = self.padre.costo + 1
        else:
            self.costo = self.padre.costo + 2

    def calcular_heuristica(self):
        if 'M' in self.estado and 'R' in self.estado:
            self.heuristica = (abs(self.get_X('M') - self.get_X('X')) + abs(self.get_Y('M') - self.get_Y('X')))
        elif 'M' in self.estado:
            self.heuristica = (abs(self.get_X('M') - self.get_X('R')) + abs(self.get_Y('M') - self.get_Y('R')))
        else:
            self.heuristica = 0

    def get_X(self, letra):
        return (self.estado.index(letra) // 10) + 1

    def get_Y(self, letra):
        return (self.estado.index(letra) % 10) + 1

    def crear_frame(self, contenedor):
        operadores = ['↑', '→', '↓', '←']
        frame = Frame(contenedor, width="350", height="244")
        for fila in range(0, 10):
            for columna in range(0, 10):
                pos = columna + (10 * fila)
                if self.estado[pos] == 0:
                    Button(frame, text="", width=2, height=1, bg="white").grid(row=fila, column=columna)
                elif self.estado[pos] == 1:
                    Button(frame, text="", width=2, height=1, bg="black").grid(row=fila, column=columna)
                elif self.estado[pos] == 2:
                    padres = self.padre
                    while padres.estado[pos] != 'X':
                        padres = padres.padre
                    Button(frame, text=operadores[padres.operador], width=2, height=1, bg="white").grid(rpw=fila, column=columna)
                elif self.estado[pos] == 'R':
                    Button(frame, text="R", width=2, height=1, bg="white").grid(row=fila, column=columna)
                elif self.estado[pos] == 'M':
                    Button(frame, text="M", width=2, height=1, bg="white").grid(row=fila, column=columna)
                else:
                    Button(frame, text="X", width=2, height=1, bg="white").grid(row=fila, column=columna)
        Label(frame, text="Profundidad: "+ str(self.profundidad)).grid(row=11, column=0, columnspan=10)
        frame.grid_propagate(False)
        return frame

    def crear_estado_inicial(self, contenedor):
        self.estado =  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.botones = []
        self.opcion_seleccionada = 3
        frame = Frame(contenedor)
        listaBloquear = [11, 21, 31, 41, 51, 24, 25, 18, 28, 38, 48, 63, 64, 65, 67, 77, 87, 97, 44]
        contador = 0
        for fila in range(0, 10):
            for columna in range(0, 10):
                self.botones.append(Button(frame, text="", width=2, height=1, bg="white"))
                self.botones[-1].grid(row=fila, column=columna)
        Label(frame, text="Opciones:").grid(row=10, columnspan=10)
        self.botones.append(Button(frame, text="R", width=2, height=1, bg="white"))
        self.botones[-1].grid(row=11, column=4)
        self.botones.append(Button(frame, text="M", width=2, height=1, bg="white"))
        self.botones[-1].grid(row=11, column=5)
        self.botones.append(Button(frame, text="", width=2, height=1, bg="white"))
        self.botones[-1].grid(row=11, column=6)
        for boton in range(0, 103):
            if contador in listaBloquear:
                self.botones[boton].config(text="", bg="black")
                self.estado[contador] = 1
            else:    
                self.botones[boton].config(command=lambda boton=boton: self.pulsar(boton))
            contador = contador + 1
        return frame

    def pulsar(self, posicion):
        if posicion < 100:
            if self.opcion_seleccionada == 1 and not 'R' in self.estado:
                self.botones[posicion].config(text="R", bg="white")
                self.estado[posicion] = 'R'
            elif self.opcion_seleccionada == 2 and not 'M' in self.estado:
                self.botones[posicion].config(text="M", bg="white")
                self.estado[posicion] = 'M'
            elif self.opcion_seleccionada == 3:
                self.botones[posicion].config(text="", bg="white")
                self.estado[posicion] = 0
        elif posicion == 100:
            self.opcion_seleccionada = 1
        elif posicion == 101:
            self.opcion_seleccionada = 2
        elif posicion == 102:
            self.opcion_seleccionada = 3