#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Adrián Gerpe Val"

'''
Exercicio 4. Escribe un script que pide ao usuario os coeficientes dunha ecuación de segundo grao e calcula a solución.
Comproba se hai unha solución, dúas ou ningunha. Dependendo do caso, mostra as solucións que corresponda.
'''

def descriminante(a: float, b: float, c: float) -> float:
    """
    Calcula o discriminante dunha ecuación de segundo grao.

    Args:
        a (float): Coeficiente A da ecuación.
        b (float): Coeficiente B da ecuación.
        c (float): Coeficiente C da ecuación.

    Returns:
        float: O discriminante da ecuación.
    """
    return b**2 - 4*a*c

def numero_solucions(a: float, b: float, c: float) -> int:
    """
    Calcula o número de solucións dunha ecuación de segundo grao.

    Args:
        a (float): Coeficiente A da ecuación.
        b (float): Coeficiente B da ecuación.
        c (float): Coeficiente C da ecuación.

    Returns:
        int: O número de solucións da ecuación.
    """
    discriminante_valor = descriminante(a, b, c)
    if discriminante_valor > 0:
        return 2
    elif discriminante_valor == 0:
        return 1
    else:
        return 0

def solucion_unica(a: float, b: float) -> float:
    """
    Calcula a solución única dunha ecuación de segundo grao.

    Args:
        a (float): Coeficiente A da ecuación.
        b (float): Coeficiente B da ecuación.

    Returns:
        float: A solución única da ecuación.
    """
    return -b / (2*a)

def calcula_duas_solucions(a: float, b: float, c: float) -> float:
    """
    Calcula as dúas solucións dunha ecuación de segundo grao.

    Args:
        a (float): Coeficiente A da ecuación.
        b (float): Coeficiente B da ecuación.
        c (float): Coeficiente C da ecuación.

    Returns:
        tuple: As dúas solucións da ecuación.
    """
    discriminante_valor = descriminante(a, b, c)
    solucion1 = (-b + discriminante_valor**0.5) / (2*a)
    solucion2 = (-b - discriminante_valor**0.5) / (2*a)
    return solucion1, solucion2

# Pedimos os coeficientes ao usuario: 
a = float(input("Introduce o coeficiente A: "))
b = float(input("Introduce o coeficiente B: "))
c = float(input("Introduce o coeficiente C: "))

# Calculamos o número de solucións: 
num_solucions = numero_solucions(a, b, c)

# Mostramos as solucións: 
if num_solucions == 2:
    solucion1, solucion2 = calcula_duas_solucions(a, b, c)
    print("As dúas solucións son:")
    print("x1 =", solucion1)
    print("x2 =", solucion2)
elif num_solucions == 1:
    solucion = solucion_unica(a, b)
    print("A solución é:")
    print("x =", solucion)
else:
    print("A ecuación non ten solucións ")