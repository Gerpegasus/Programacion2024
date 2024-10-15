#!/usr/bin/env python
#-*-  coding: utf-8 -*-

__author__ = "Adrian Gerpe Val"

"""
Exercicio 12 Escribe un script que elixirá no seu comezo un número ao azar entre 1 e 25. 
A continuación o usuario introducirá números por teclado ata que acerte o número seleccionado ao azar. 
Cada vez que se introduza un número incorrecto, o script proporcionaralle pistas ao usuario: “o número e maior” ou “o número é menor”. 
Unha vez que o usuario acerte o número, indicaráselle por pantalla se gañou o xogo ou non. 
Para gañar, o usuario deberá acertar o número en menos de 5 intentos.
"""

import random

# Collemos un numero aleatorio entre 1 e 25
numero_aleatorio = random.randint(1, 25)

# Inicializamos un contador para saber o numero de intentos
contador = 1

# Pedimoslle ao usuario que introduza un numero enteiro
numero_introducido = int(input("Introduce un número enteiro: "))

# Creamos un bucle que faga o seguinte: 
while True:
    # Se o numero aleatorio e maior que o introducido imprime un mensaxe e suma 1 a contador
    if numero_aleatorio > numero_introducido:
        print("O numero e maior")
        numero_introducido = int(input("Introduce un número enteiro: "))
        contador = contador + 1
    # Se o numero aleatorio e menor que o introducido imprime un mensaxe e suma 1 a contador
    elif numero_aleatorio < numero_introducido:
        print("O numero e menor")
        numero_introducido = int(input("Introduce un número enteiro: "))
        contador = contador + 1
    # Se non e ningunha das condicions anteriores, significaria que o usuario acertou o numero
    else:
        print(f"O numero {numero_aleatorio} e igual a {numero_introducido}, acertaches o numero.")
        break
if contador <= 5:
    print("Gañaches, acertaches en menos de 5 intentos")
else:    
    print(f"Perdeches, o teu numero de intentos foi {contador}")