#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Adrián Gerpe Val"

'''
Exercicio 19. A avaliación deste módulo é a seguinte: 15% de tarefas, 20% exame teórico e 65% exame práctico. 
Escribe un script que lle pida ao usuario as súas tres notas sobre 10 e indicaralle por pantalla a súa nota final sobre 10.
'''
# Pedimos os datos ao usuario: 
nota_tarefas = float(input("Introduce a nota de tarefas: "))

nota_teorico = float(input("Introduce a nota do exame teorico: "))

nota_practico = float(input("Introduce a nota do exame practico: "))

# Calculamos a nota final: 
nota_final = float((nota_tarefas * 0.15) + (nota_teorico * 0.20) + (nota_practico * 0.65))

# Imprimimos o resultado na pantalla: 
print (f"A nota final é: {nota_final}")