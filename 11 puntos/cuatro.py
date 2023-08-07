# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 17:07:05 2023

@author: aleja
"""

class Rectangulo:
    def __init__(self, punto_esquina_sup_izq, punto_esquina_inf_der):
        self.esquina_sup_izq = punto_esquina_sup_izq
        self.esquina_inf_der = punto_esquina_inf_der

    def calcular_perimetro(self):
        base = abs(self.esquina_inf_der[0] - self.esquina_sup_izq[0])
        altura = abs(self.esquina_inf_der[1] - self.esquina_sup_izq[1])
        return 2 * (base + altura)

    def calcular_area(self):
        base = abs(self.esquina_inf_der[0] - self.esquina_sup_izq[0])
        altura = abs(self.esquina_inf_der[1] - self.esquina_sup_izq[1])
        return base * altura

    def es_cuadrado(self):
        base = abs(self.esquina_inf_der[0] - self.esquina_sup_izq[0])
        altura = abs(self.esquina_inf_der[1] - self.esquina_sup_izq[1])
        return base == altura


punto_sup_izq = [1, 5]
punto_inf_der = [6, 2]

rectangulo1 = Rectangulo(punto_sup_izq, punto_inf_der)

print(f"Perímetro del rectángulo: {rectangulo1.calcular_perimetro()}")
print(f"Área del rectángulo: {rectangulo1.calcular_area()}")

if rectangulo1.es_cuadrado():
    print("El rectángulo es un cuadrado.")
else:
    print("El rectángulo no es un cuadrado.")
