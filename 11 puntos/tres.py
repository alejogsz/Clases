# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 16:57:53 2023

@author: aleja
"""

import math 
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mostrar_coordenadas(self):
        print(f"Coordenadas: ({self.x}, {self.y})")
    
    def mover_coordenadas(self, nuevo_x, nuevo_y):
        self.x = nuevo_x
        self.y = nuevo_y

    def calcular_distancia(self, otro_punto):
        distancia = math.sqrt((self.x - otro_punto.x)**2 + (self.y - otro_punto.y)**2)
        return distancia
    

punto1 = Punto(3, 3)
punto1.mostrar_coordenadas()

punto2 = Punto(-10, 1)
punto2.mostrar_coordenadas()


punto1.mover_coordenadas(4, 5)
punto1.mostrar_coordenadas()


distancia = punto1.calcular_distancia(punto2)
print(f"Distancia entre los puntos: {distancia}")