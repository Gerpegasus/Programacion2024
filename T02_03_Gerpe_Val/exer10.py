#!/usr/bin/env python
#-*-  coding: utf-8 -*-

__author__ = "Adrian Gerpe Val"

"""
Exercicio 10 Escribe un script no que o usuario poida introducir números enteiros por teclado ata que teclee a palabra “fin”. 
Tras finalizar a introdución de números, indícalle cal é o número máis pequeno introducido.
"""

# Inicializamos a variable para gardar o numero pequeno
numero_pequeno = "Ningun"

# Creamos un bucle
while True:
    # Pedimos ao usuario que introduza un numero ou a palabra "fin"
    entrada_usuario = input("Introduza un número enteiro ou 'fin' para rematar: ")

    # Se o usuario introduciu a palabra "fin", saímos do programa
    if entrada_usuario == "fin":
        print("Sairase do programa. ")
        break

    # Intentamos converter o input nun numero enteiro
    try:
        numero_introducido = int(entrada_usuario)
    except ValueError:
        print("Erro: non é un número enteiro. Volve a intentar.")
        continue

    # Se o numero pequeno non ten ningun valor, dalle o valor do numero introducido
    if numero_pequeno == "Ningun":
        numero_pequeno = numero_introducido
    # Se o numero introducido e menor que o actual actualizamos a variable
    elif numero_introducido < numero_pequeno:
        numero_pequeno = numero_introducido

# Mostramos o resultado
print("O número máis pequeno introducido foi:", numero_pequeno)

