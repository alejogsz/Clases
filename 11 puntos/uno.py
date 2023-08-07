# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 16:53:02 2023

@author: aleja
"""

class Vehiculo:
    def __init__(self, velocidad_maxima, kilometraje):
        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje

  

vehiculo1 = Vehiculo(451, 6500)

print("la velocidad maxima es ", vehiculo1.velocidad_maxima ," y el kilometraje es ", vehiculo1.kilometraje, " km")