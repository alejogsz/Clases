# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 17:28:50 2023

@author: aleja
"""
# Cree una clase Circulo que tenga las propiedades centro y radio, las cuales se inicializan con
#  parámetros en el constructor. Defina métodos en la clase para calcular el área, el perímetro 
#  e indicar si un punto pertenece al círculo o no.
import math

class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio**2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

    def punto_pertenece(self, punto):
        distancia_al_centro = math.sqrt((punto[0] - self.centro[0])**2 + (punto[1] - self.centro[1])**2)
        return distancia_al_centro <= self.radio


CENTRO=[0,0]
circulo1 = Circulo(CENTRO, 5)

print(f"Área del círculo: {circulo1.calcular_area()}")
print(f"Perímetro del círculo: {circulo1.calcular_perimetro()}")

punto_dentro = [3, 4]
if circulo1.punto_pertenece(punto_dentro):
    print("El punto está dentro del círculo.")
else:
    print("El punto no está dentro del círculo.")