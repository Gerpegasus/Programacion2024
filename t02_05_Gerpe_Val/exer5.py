#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Adrián Gerpe Val"

'''
Exercicio 5. Escribe unha función calcular_desconto_irpf(soldo_bruto: float/int, irpf: int) -> float nun script o soldo bruto e o IRPF en tanto por cen. 
Comproba que estes dous valores son números, que o soldo é maior que 0 e que o IRPF é un valor válido. Se algunha destas condicións non se cumpre, lanza a excepción ValueError. 
O propio script deberá recibir estes datos por teclado, e utilizar a función creada para calcular o desconto do IRPF. 
Captura a excepción que lanza a función.
'''

def calcular_desconto_irpf(soldo_bruto, irpf):
    """
    Calcula o desconto do IRPF a partir do soldo bruto e o tipo de IRPF.
    """
    if not isinstance(soldo_bruto, (int, float)) or soldo_bruto <= 0:
        raise ValueError("O soldo bruto debe ser un número maior que 0.")
    
    if not isinstance(irpf, (int, float)) or irpf < 0 or irpf > 100:
        raise ValueError("O IRPF debe ser un número entre 0 e 100.")
    
    desconto = (soldo_bruto * irpf) / 100
    return desconto

try:
    soldo_bruto = float(input("Introduce o soldo bruto: "))
    irpf = float(input("Introduce o IRPF (en tanto por cen): "))
    
    desconto = calcular_desconto_irpf(soldo_bruto, irpf)
    print("O desconto do IRPF é:", desconto)
except ValueError as e:
    print("Erro:", e)