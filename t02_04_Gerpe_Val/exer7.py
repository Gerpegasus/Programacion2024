#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Adrián Gerpe Val"

'''
Exercicio 7 Escribe un script que calcule o salario dun traballador. 
O programa recibirá por parte do usuario as horas traballadas ao día e os € por cada hora de traballo. 
A continuación preguntaralle ao usuario se a tarifa é en bruto ou en neto. 
A partir da súa resposta calcula o salario mensual neto.

Os días laborables ao mes son 22.
Se o usuario indica que o custe da hora é en bruto, indícalle ao usuario que introduza o IRPF en tanto por cen para poder calcularlle o salario neto.
Deduce o número necesario de funcións e defíneas.
'''

def calcular_salario_neto(horas_traballadas: float, euros_hora: float, irpf: float) -> float:
    """
    Calcula o salario neto a partir do salario bruto e o IRPF.

    Args:
        horas_traballadas (float): Cantidade de horas traballadas ao día.
        euros_hora (float): Salario por hora en bruto.
        irpf (float): Porcentaxe de IRPF a deducir.

    Returns:
        float: Salario mensual neto.
    """
    salario_bruto = euros_hora * horas_traballadas * 22
    salario_neto = salario_bruto - (salario_bruto * irpf / 100)
    return salario_neto

def calcular_salario_bruto(horas_traballadas: float, euros_hora: float) -> float:
    """
    Calcula o salario mensual bruto.

    Args:
        horas_traballadas (float): Cantidade de horas traballadas ao día.
        euros_hora (float): Salario por hora.

    Returns:
        float: Salario mensual bruto.
    """
    return euros_hora * horas_traballadas * 22

# Pedimos os datos ao usuario
horas_traballadas = float(input("Introduce as horas traballadas ao día: "))
euros_hora = float(input("Introduce o teu salario por hora: "))
resposta = input("¿A tarifa é en bruto ou en neto? ")

# Dependendo da resposta do usuario, calculamos o salario neto ou bruto
if resposta == "neto":
    salario_neto = calcular_salario_bruto(horas_traballadas, euros_hora)
    print(f"O teu salario mensual é de {salario_neto:.2f} euros")
elif resposta == "bruto":
    irpf = float(input("Introduce o teu IRPF (en %): "))
    salario_neto = calcular_salario_neto(horas_traballadas, euros_hora, irpf)
    print(f"O teu salario mensual neto é de {salario_neto:.2f} euros")
else:
    print("Introduce unha tarifa válida")