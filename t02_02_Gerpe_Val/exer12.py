#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Adrián Gerpe Val"

'''
Exercicio 12. Escribe un script que pida o nome de usuario e contrasinal ao usuario. Indica se o inicio de sesión é correcto. O nome de usuario sería “python” e o contrasinal “pip”.
'''
# Pedimos o Usuario e a Contrasinal
usuario = input("Usuario: ")
contrasinal = input("Contrasinal: ")

# Comprobamos se os  datos son correctos
if  usuario == "python" and contrasinal == "pip":
    print("Inicio de sesión correcto")
else:
    print("Inicio de sesión incorrecto")


