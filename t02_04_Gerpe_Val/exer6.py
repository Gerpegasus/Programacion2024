#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Adrián Gerpe Val"

'''
Exercicio 6 Escribe un script que pida o nome de usuario e contrasinal ao usuario. 
Indica se o inicio de sesión é correcto. O nome de usuario correcto sería “python” e o contrasinal “pip”. 
Crea a función login(usuario: str, contrasinal: str) -> boolean para realizar esta operación.
'''

def login(usuario: str, contrasinal: str) -> bool:
    """
    Verifica se o nome de usuario e a contrasinal son correctos.

    Args:
        usuario (str): O nome de usuario introducido.
        contrasinal (str): A contrasinal introducida.

    Returns:
        bool: True se o inicio de sesión é correcto, False en caso contrario.
    """
    return usuario == "python" and contrasinal == "pip"

# Pedimos o Usuario e a Contrasinal
usuario = input("Usuario: ")
contrasinal = input("Contrasinal: ")

# Comprobamos se os datos son correctos
if login(usuario, contrasinal):
    print("Inicio de sesión correcto")
else:
    print("Inicio de sesión incorrecto")