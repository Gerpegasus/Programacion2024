#!/usr/bin/env python
#-*-  coding: utf-8 -*-

__author__ = "Adrian Gerpe Val"

"""
Exercicio 11 Escribe un script que calcule o mínimo común múltiplo de dous números introducidos polo usuario.
"""
# Pedimos o usuario que introduza os numeros
numero_1 = int(input("Introduce o primeiro número: "))

numero_2 = int(input("Introduce o segundo número: "))

# Inicializamos a variable contador
contador = 1

# Mentres non sea certo, se o contador entre o numero 1 non da resto cero e o contador entre o numero 2 non da resto cero, 
# sumase 1 a contador hasta que dee como resto 0
while not (contador % numero_1 == 0 and contador % numero_2 == 0):
    contador += 1
print(f"O MCM de {numero_1} e {numero_2} e {contador} ")