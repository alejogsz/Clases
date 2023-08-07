# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 17:42:39 2023

@author: aleja
"""
# Cree una clase Carta que contenga dos propiedades valor y pinta, las cuales son asignadas solo 
# al momento de la construcción del objeto (se pasan como parámetros en el constructor). Defina 
# 4 constantes que representan los nombres de las 4 pintas que puede tener una carta.
class Carta:
    PINTAS = ("Corazones", "Diamantes", "Treboles", "Picas")

    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta

carta1 = Carta("As", Carta.PINTAS[0])
print(f"Valor: {carta1.valor}, Pinta: {carta1.pinta}")

carta2 = Carta("Queen", Carta.PINTAS[3])
print(f"Valor: {carta2.valor}, Pinta: {carta2.pinta}")

carta3 = Carta(7, Carta.PINTAS[1])
print(f"Valor: {carta3.valor}, Pinta: {carta3.pinta}")

carta4 = Carta(3, Carta.PINTAS[2])
print(f"Valor: {carta4.valor}, Pinta: {carta4.pinta}")