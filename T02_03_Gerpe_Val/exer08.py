#!/usr/bin/env python
#-*-  coding: utf-8 -*-

__author__ = "Adrian Gerpe Val"

"""
Exercicio 8: Escribe un script que reciba un enteiro (n) maior ou igual a 1 e ofreza o resultado da seguinte suma: 
1 + 1/2 + 1/3 + ... 1/n
"""
#Inicializamos a variable resultado en 0.0 para que xa nos poña como float o valor
resultado = 0.0
#Inicializamos a variable contador en 1
contador = 1
#Pedimoslle o usuario que nos proporcione un numero
numero = int(input("Introduce un numero: "))
#Desarrollamos a operación
if numero >= 1:
    while contador <= numero:
        resultado += 1.0/contador
        contador += contador +1
    print(f"O resultado da operacion é: {resultado:.4f}")
else :
    print("O numero debe ser un enteiro maior o igual que 1")
