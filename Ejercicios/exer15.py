#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Adrián Gerpe Val"

'''
Exercicio 15. Escribe un script que pida ao usuario os coeficientes dunha ecuación de segundo grao e calcula as dúas solucións. Mostra as dúas solucións por pantalla.
'''

# Pedimos os coeficientes ao usuario
A = float(input("Introduce o coeficiente A: "))
B = float(input("Introduce o coeficiente B: "))
C = float(input("Introduce o coeficiente C: "))

# Calculamos o discriminante
discriminante = B**2 - 4*A*C

# Calculamos as solucions
if discriminante >= 0:
    solucion1 = (-B + discriminante**0.5) / (2*A)
    solucion2 = (-B - discriminante**0.5) / (2*A)
    print("As duas solucións son:")
    print("x1 =", solucion1)
    print("x2 =", solucion2)
else:
    print("A ecuación non ten solucións ")