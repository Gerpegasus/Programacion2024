#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Adrián Gerpe Val"

'''
Exercicio 9. Vaise realizar un sorteo no que pode haber un número diferente de gañadores a partir dunhas rifas numeradas entre 0001e 9999. 
Escribe un script que reciba por teclado o número de premios dispoñibles e imprima os números premiados co formato de 4 díxitos.
'''

import random

def obter_premios(numero_premios):
    """
    Obtén unha lista de números premiados únicos.

    :param numero_premios: Número de premios dispoñibles.
    :return: Lista de números premiados en formato de 4 díxitos.
    :raises ValueError: Se o número de premios non é válido.
    """
    if numero_premios <= 0:
        raise ValueError("O número de premios debe ser maior que 0.")
    
    premios = set()  # Usamos un conjunto para garantir que os números son únicos
    
    while len(premios) < numero_premios:
        numero_aleatorio = random.randint(1, 9999)
        premios.add(f"{numero_aleatorio:04d}")  # Formato de 4 díxitos
    
    return list(premios)

def main():
    try:
        numero_premios = int(input("Introduce o número de premios dispoñibles: "))
        premios = obter_premios(numero_premios)
        
        print("\nNúmeros premiados:")
        for premio in premios:
            print(premio)
    
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()