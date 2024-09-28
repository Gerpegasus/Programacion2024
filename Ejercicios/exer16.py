#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Adrián Gerpe Val"

'''
Exercicio 16. Escribe un script que pida ao usuario o seu nome e apelidos por separado e mostra a seguinte mensaxe por pantalla: 
O usuario <apelido1> <apelido 2>, <nome> rexistrouse correctamente
'''

apelido1 = input("Introduce o primeiro apelido:" )
apelido2 = input("Introduce o segundo apelido: ")
nome = input("Introduce o nome : ")

print(f" O usuario {apelido1} {apelido2}, {nome} rexistrouse correctamente")