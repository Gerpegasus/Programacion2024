#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Adrián Gerpe Val"

'''
Exercicio 10. O algoritmo de ordenación que se describe a continuación permite ordenar unha lista de xeito simple pero ineficiente para listas pequenas. 
Funciona comparando elementos adxacentes na lista e intercambiándoos se están na orde incorrecta (é dicir, se o primeiro elemento é maior que o segundo). 
Este proceso repítese varias veces ata que toda a lista estea ordenada. 
É dicir, realízanse varias pasadas sobre a lista para ordenala ata que non se produza ningún intercambio de posicións.
'''

def ordenar(lista):
    """
    Ordena una lista de números de menor a mayor

    :param lista: Lista de números a ordenar.
    :return: Lista ordenada de números.
    """
    n = len(lista)  

    # Realizamos varias pasadas sobre a lista
    for i in range(n):
        for j in range(0, n - 1): 
            # Se o elemento actual e maior que o seguiente
            if lista[j] > lista[j + 1]:
                # Intercambiamos os elementos
                temp = lista[j]
                lista[j] = lista[j + 1] 
                lista[j + 1] = temp

    return lista  # Devolvemos a lista ordenada

lista = [64, 34, 25, 12, 22, 11, 90]
lista_ordenada = ordenar(lista)
print(lista_ordenada)