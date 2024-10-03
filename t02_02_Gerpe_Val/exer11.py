#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Adrián Gerpe Val"

'''
Exercicio 11. Escribe un script que faga o cambio de divisas tanto de euros a libras e viceversa. 
Crea un menú para que o usuario escolla o cambio que desexa realizar e a continuación introducirá o valor da moeda correspondente para realizar o cambio de divisas. 
1 € son 0,83 libras.
'''

# Creamos o menú
print("Elixe un dos seguintes cambios de divisa: ")
print("\ta) Euros a Libras")
print("\tb) Libras a Euros")
print("\tc) Sair do menú")

# Escollemos a opcion correcta
opcion = input(">")

# Dependendo da solución, facemos o cambio de divisas oportuno
if opcion  == "a":
    euros = float(input("Introduce o valor en euros: "))
    libras = euros * 0.83
    print(f"{euros} euros son {libras} libras")
elif opcion == "b":
    libras = float(input("Introduce o valor en libras: "))
    euros = libras / 0.83
    print(f"{libras} euros son {euros} dolares")
elif opcion == "c":
    print("Sair do menú")
else:
    print("Opción non válida. Sair do menú")