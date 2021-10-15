# -*- coding: utf-8 -*-
import time
from tkinter import *
class Busqueda(object):
    def __init__(self, inicio):
        self.abiertos = []
        self.cerrados = []
        self.tiempo_total = 0
        self.inicio = inicio

    def buscar(self):
        encontro = False
        self.abiertos.append(self.inicio)
        while self.abiertos and not encontro:
            actual = self.abiertos.pop(0)
            self.cerrados.append(actual)
            if actual.test_objetivo():
                encontro = True
            else:
                self.aplicar_estrategia(actual.crear_sucesores())
    
    def crear_frame(self, contenedor):
        frame = Frame(contenedor, width="500", height="400")
        Label(frame, text="Resultado:").pack(side=BOTTOM)
        if not self.abiertos:
            Label(frame, text="No se encontró solución").pack()
        else:
            self.cerrados[-1].crear_frame(frame).pack()
            (Label(frame, text="Nodos totales: "+ str(len(self.abiertos) + len(self.cerrados))).pack(side=BOTTOM))
            (Label(frame, text="Nodos abiertos: "+ str(len(self.abiertos))).pack(side=BOTTOM))
            (Label(frame, text="Nodos cerrados: "+ str(len(self.cerrados))).pack(side=BOTTOM))
            Label(frame, text="Tiempo: "+ str(self.tiempo_total)).pack(side=BOTTOM)
        frame.pack_propagate(False)
        return frame

    def cronometro(self, funcion, *argumentos):
        inicio = time.time()
        funcion(*argumentos)
        fin = time.time()
        self.tiempo_total = fin - inicio

    def ordenar(self, sucesores):
        pass

class Profundidad(Busqueda):
    def __init__(self, inicial):
        super().__init__(inicial)

    def aplicar_estrategia(self, sucesores):
        while sucesores:
            self.abiertos.insert(0, sucesores.pop())

class Amplitud(Busqueda):
    def __init__(self, inicial):
        super().__init__(inicial)

    def aplicar_estrategia(self, sucesores):
        self.abiertos.extend(sucesores)

class AAsterisco(Busqueda):
    def __init__(self, inicial):
        super().__init__(inicial)
        self.inicio.calcular_f()

    def aplicar_estrategia(self, sucesores):
        for sucesor in sucesores:
            sucesor.calcular_f()
            i = 0
            while i < len(self.abiertos) and self.abiertos[i].f < sucesor.f:
                i += 1
            while (i < len(self.abiertos) and self.abiertos[i].f == sucesor.f and self.abiertos[i].heuristica < sucesor.heuristica):
                i += 1
            self.abiertos.insert(i, sucesor)

class PrimeroElMejor(Busqueda):
    def __init__(self, inicial):
        super().__init__(inicial)

    def aplicar_estrategia(self, sucesores):
        for sucesor in sucesores:
            sucesor.calcular_heuristica()
            i = 0
            while (i < len(self.abiertos) and self.abiertos[i].heuristica < sucesor.heuristica):
                i += 1
            self.abiertos.insert(i, sucesor)