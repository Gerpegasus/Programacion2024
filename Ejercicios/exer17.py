#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Adrián Gerpe Val"

'''
Exercicio 17. Escribe un script que pida ao usuario o número de quilómetros recorridos na súa última viaxe en coche,
o consumo do coche en litros cada 100 quilómetros e o prezo en euros dun litro de combustible. Calcula o custo da viaxe e móstrallo ao usuario por pantalla.
'''
# Pedimos os datos ao usuario: 
km_recorridos = float(input("Introduce os Km recorridos na ultima viaxe: "))

consumo = float(input("Introduce o cosumo cada 100km: "))

precio = float(input("Introduce o precio en euros dun litro de combustible: "))

# Calculamos o consumo total de combustible: 
consumo_total = (km_recorridos / 100) * consumo

# Calculamos o custo da viaxe: 
custo_viaxe = consumo_total * precio

# Mostramos o custo da viaxe ao usuario: 
print (f"A tua viaxe vai custar {custo_viaxe}€.")