#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Adrián Gerpe Val"

'''
Exercicio 16. Escribe un script que pida ao usuario o seu nome e apelidos por separado e mostra a seguinte mensaxe por pantalla: 
O usuario <apelido1> <apelido 2>, <nome> rexistrouse correctamente
'''
# Pedimos os datos ao usuario: 
apelido1 = input("Introduce o primeiro apelido:" )
apelido2 = input("Introduce o segundo apelido: ")
nome = input("Introduce o nome : ")

# Imprimimos os datos na pantalla: 
print(f" O usuario {apelido1} {apelido2}, {nome} rexistrouse correctamente")