#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Adrián Gerpe Val"

'''
Exercicio 18. Escribe un script que pida ao usuario 3 números e móstralle por pantalla a media dos 3 números.
'''
# Pedimos os datos ao usuario: 
numero1 = int(input("Introduce o primeiro numero: "))

numero2 = int(input("Introduce o segundo numero: "))

numero3 = int(input("Introduce o terceiro numero: "))

# Facemos a media dos tres numeros: 
media = int((numero1 + numero2 + numero3) / 3)

# Imprimimos a información na pantalla: 
print (f"A media dos tres numeros e: {media}")