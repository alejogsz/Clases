# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 16:54:08 2023

@author: aleja
"""

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    

punto1 = Punto(4, 5)

print(f"las cordenadas en el plano son {punto1.x}, {punto1.y}")