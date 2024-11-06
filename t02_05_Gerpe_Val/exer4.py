#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Adrián Gerpe Val"

'''
Exercicio 4. Escribe unha función raiz_cadrada(numero: float/int) -> float nun script que calcule a raíz cadrada dun número. 
Se o parámetro non é un número ou é negativo, lanza unha excepción chamada ValueError. 
O propio script debe recibir un número por parte do usuario e calcula a raíz cadrada dese número utilizando a función creada anteriormente. 
Captura a excepción que lanza a función.
'''

def raiz_cadrada(numero):
    """
    Calcula a raíz cadrada dun número.
    """
    if not isinstance(numero, (int, float)) or numero < 0:
        raise ValueError("O número debe ser un número non negativo.")
    
    estimacion = numero / 2  # Comeza cunha estimación
    for _ in range(10):  # Realiza 10 iteracións
        estimacion = (estimacion + numero / estimacion) / 2
    
    return estimacion

numero_usuario = input("Introduce un número: ")

try:
    numero_usuario = float(numero_usuario)  # Convértese a float
    resultado = raiz_cadrada(numero_usuario)
    print("A raíz cadrada é:", resultado)
except ValueError as e:
    print("Erro:", e)