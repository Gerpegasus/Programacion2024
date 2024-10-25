#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Adrián Gerpe Val"

'''
Exercicio 8 A avaliación deste módulo é a seguinte: 15% de tarefas, 20% exame teórico e 65% exame práctico. 
Escribe un script que lle pedirá ao usuario as súas tres notas sobre 10. Indicaralle por pantalla se obtivo Sobresaliente, Notable, Ben, Suficiente ou Insuficiente.

Deduce o número necesario de funcións e defíneas.
'''

def calcular_nota_final(nota_tarefas: float, nota_teorico: float, nota_practico: float) -> float:
    """
    Calcula a nota final a partir das notas de tarefas, exame teórico e exame práctico.

    Args:
        nota_tarefas (float): Nota das tarefas (0 a 10).
        nota_teorico (float): Nota do exame teórico (0 a 10).
        nota_practico (float): Nota do exame práctico (0 a 10).

    Returns:
        float: Nota final calculada sobre 10.
    """
    return (nota_tarefas * 0.15) + (nota_teorico * 0.20) + (nota_practico * 0.65)

def determinar_calificacion(nota_final: float) -> str:
    """
    Determina a calificación a partir da nota final.

    Args:
        nota_final (float): Nota final (0 a 10).

    Returns:
        str: Calificación correspondente (Sobresaliente, Notable, Ben, Suficiente ou Insuficiente).
    """
    if nota_final >= 9:
        return "Sobresaliente"
    elif nota_final >= 7:
        return "Notable"
    elif nota_final >= 5:
        return "Ben"
    elif nota_final >= 3:
        return "Suficiente"
    else:
        return "Insuficiente"

# Pedimos os datos ao usuario
nota_tarefas = float(input("Introduce a nota de tarefas (0 a 10): "))
nota_teorico = float(input("Introduce a nota do exame teórico (0 a 10): "))
nota_practico = float(input("Introduce a nota do exame práctico (0 a 10): "))

# Calculamos a nota final
nota_final = calcular_nota_final(nota_tarefas, nota_teorico, nota_practico)

# Determinamos a calificación
calificacion = determinar_calificacion(nota_final)

# Imprimimos o resultado na pantalla
print(f"A nota final é: {nota_final:.2f}")
print(f"A calificación é: {calificacion}")