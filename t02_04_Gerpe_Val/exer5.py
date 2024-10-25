#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Adrián Gerpe Val"

'''
Exercicio 5 Escribe un script que faga o cambio de divisas tanto de euros a libras e viceversa. 
Crea un menú para que o usuario escolla o cambio que desexa realizar. Realiza unha función para cada un dos cambios:
'''

def libras_a_euros(libras: float) -> float:
    """
    Convierte libras a euros.

    Args:
        libras (float): Cantidad en libras que se desea convertir.

    Returns:
        float: Cantidad equivalente en euros.
    """
    return libras / 1.10

def euros_a_libras(euros: float) -> float:
    """
    Convierte euros a libras.

    Args:
        euros (float): Cantidad en euros que se desea convertir.

    Returns:
        float: Cantidad equivalente en libras.
    """
    return euros * 1.10

# Creamos o menú
while True:
    print("\nElixe un dos seguintes cambios de divisa: ")
    print("\ta) Euros a Libras")
    print("\tb) Libras a Euros")
    print("\tc) Sair do menú")

    # Escollemos a opción correcta
    opcion = input("> ")

    # Dependendo da opción, facemos o cambio de divisas oportuno
    if opcion == "a":
        euros = float(input("Introduce o valor en euros: "))
        libras = euros_a_libras(euros)
        print(f"{euros} euros son {libras:.2f} libras")
    elif opcion == "b":
        libras = float(input("Introduce o valor en libras: "))
        euros = libras_a_euros(libras)
        print(f"{libras} libras son {euros:.2f} euros")
    elif opcion == "c":
        print("Sair do menú")
        break
    else:
        print("Opción non válida. Intenta de novo.")