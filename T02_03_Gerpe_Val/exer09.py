#!/usr/bin/env python
#-*-  coding: utf-8 -*-

__author__ = "Adrian Gerpe Val"

"""
Exercicio 9: Escribe un script que permita obter o factorial dun número enteiro positivo introducido por teclado.
"""
#Inicializamos a variable do contador en 1
contador = 1
#Iniializamos a variable do resultado en 1
resultado = 1
#Pedimoslle o usuario que nos proporcione un numero
numero = int(input("Introduce un numero: "))
#Desarrollamos a operación para obter o factorial do numero
if numero >= 0:
    while contador <= numero :
        resultado = resultado * contador
        contador = contador + 1
    print(f"O factorial de {numero} é {resultado}")
else:
    print("Introduce un numero valido")
