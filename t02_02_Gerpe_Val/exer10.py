#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Adrián Gerpe Val"

'''
Exercicio 10. Escribe un script que pide ao usuario por teclado os coeficientes dunha ecuación de segundo grao e calcula a solución.
Comproba se hai unha solución, dúas ou ningunha. Dependendo do caso, mostra as solucións que corresponda.
'''

# Pedimos os coeficientes ao usuario: 
a = float(input("Introduce o coeficiente A: "))
b = float(input("Introduce o coeficiente B: "))
c = float(input("Introduce o coeficiente C: "))

# Calculamos o discriminante: 
discriminante = b**2 - 4*a*c

# Calculamos as solucions: 
if discriminante > 0:
    solucion1 = (-b + discriminante**0.5) / (2*a)
    solucion2 = (-b - discriminante**0.5) / (2*a)
    print("As duas solucións son:")
    print("x1 =", solucion1)
    print("x2 =", solucion2)

elif discriminante == 0:
    print("A solución é 0")
       
else:
    print("A ecuación non ten solucións ")

