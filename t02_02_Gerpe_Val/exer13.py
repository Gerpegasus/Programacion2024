#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Adrián Gerpe Val"

'''
Exercicio 13. Escribe un script que calcule o salario dun traballador. O programa recibirá as horas traballadas ao día e os € por hora dese traballo por parte do usuario.
A continuación preguntaralle ao usuario se a tarifa é en bruto ou en neto. A partir da súa resposta calcula o salario mensual neto.

Os días laborables ao mes son 22.
Se o usuario indica que o custe da hora é en bruto, indícalle ao usuario que introduza o IRPF para poder calcularlle o salario neto.
'''

# Pedimos os  datos ao usuario

horas_traballadas = float(input("Introduce as horas traballadas ao día: "))

euros_hora = float(input("Introduce o teu salario por hora: "))

resposta =  input("¿A tarifa é en bruto ou en neto? ")

# Dependendo da resposta  do usuario, calculamos o neto ou o  bruto

if resposta == "neto":
    solucion1 = euros_hora * horas_traballadas * 22
    print(f"O teu salario mensual é de {solucion1} euros")
elif resposta == "bruto":
    irpf = float(input("Introduce o teu IRPF: "))
    presolucion2 = (euros_hora * horas_traballadas * 22)
    solucion2 = presolucion2 - (presolucion2 * irpf / 100)
    print(f"O teu salario mensual é de {solucion2} euros")
else:
    print("Introduce unha tarifa valida")