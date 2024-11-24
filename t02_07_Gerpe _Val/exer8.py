#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Adrián Gerpe Val"

'''
Crea un script que pida as notas dun exame dos alumnos dunha clase para procesalos. 
Tódalas notas téñense que ir almacenando nunha lista. 
Mostra un menú que se mostre continuamente ata que o usuario seleccione a opción saír.
'''

def engadir_nota(lista, nota):
    """
    Engade unha nota á lista de notas.

    :param lista: Lista onde se almacenan as notas.
    :param nota: Nota a engadir.
    :raises ValueError: Se a lista non é unha lista ou se a nota non é válida.
    """
    if type(lista) is not list:
        raise ValueError("A entrada debe ser unha lista.")
    if type(nota) not in (int, float) or nota < 0 or nota > 10:
        raise ValueError("A nota debe ser un número entre 0 e 10.")
    
    lista.append(nota)

def mostrar_notas(lista):
    """
    Mostra as notas da lista co seu índice.

    :param lista: Lista de notas a mostrar.
    :raises ValueError: Se a lista non é unha lista.
    """
    if type(lista) is not list:
        raise ValueError("A entrada debe ser unha lista.")
    
    for indice in range(len(lista)):
        print(f"{indice} : {lista[indice]}")

def media_notas(lista):
    """
    Calcula a media das notas na lista.

    :param lista: Lista de notas.
    :raises ValueError: Se a lista non é unha lista.
    :return: Media das notas.
    """
    if type(lista) is not list:
        raise ValueError("A entrada debe ser unha lista.")
    
    if len(lista) == 0:
        return 0.0  # Se a lista está vacía, a media é 0.
    
    suma = 0
    for nota in lista:
        suma += nota
    return suma / len(lista)

def numero_aprobados(lista):
    """
    Conta o número de aprobados (notas >= 5) na lista.

    :param lista: Lista de notas.
    :raises ValueError: Se a lista non é unha lista.
    :return: Número de aprobados.
    """
    if type(lista) is not list:
        raise ValueError("A entrada debe ser unha lista.")
    
    aprobados = 0
    for nota in lista:
        if nota >= 5:
            aprobados += 1
    return aprobados

def maxima_nota(lista):
    """
    Calcula a máxima nota na lista.

    :param lista: Lista de notas.
    :raises ValueError: Se a lista non é unha lista.
    :return: Máxima nota.
    """
    if type(lista) is not list:
        raise ValueError("A entrada debe ser unha lista.")
    
    if len(lista) == 0:
        return None  # Se a lista está vacía, non hai máxima nota.
    
    max_nota = lista[0]
    for nota in lista:
        if nota > max_nota:
            max_nota = nota
    return max_nota

def eliminar_nota(lista, indice):
    """
    Elimina a nota no índice especificado.

    :param lista: Lista de notas.
    :param indice: Índice da nota a eliminar.
    :raises ValueError: Se a lista non é unha lista ou se o índice non é válido.
    """
    if type(lista) is not list:
        raise ValueError("A entrada debe ser unha lista.")
    
    if indice < 0 or indice >= len(lista):
        raise ValueError("Índice non válido.")
    
    del lista[indice]

def main():
    notas = []
    
    while True:
        print("\nMenú:")
        print("a) Engadir nota")
        print("b) Ver media")
        print("c) Ver número de aprobados")
        print("d) Ver máxima nota")
        print("e) Eliminar nota")
        print("f) Saír")
        
        opcion = input("Elixe unha opción: ")
        
        try:
            if opcion == 'a':
                nota = float(input("Introduce a nota (0-10): "))
                engadir_nota(notas, nota)
            elif opcion == 'b':
                media = media_notas(notas)
                print(f"A media das notas é: {media}")
            elif opcion == 'c':
                aprobados = numero_aprobados(notas)
                print(f"O número de aprobados é: {aprobados}")
            elif opcion == 'd':
                max_nota = maxima_nota(notas)
                if max_nota is not None:
                    print(f"A máxima nota é: {max_nota}")
                else:
                    print("Non hai notas para calcular a máxima.")
            elif opcion == 'e':
                mostrar_notas(notas)
                indice = int(input("Introduce o índice da nota a eliminar: "))
                eliminar_nota(notas, indice)
            elif opcion == 'f':
                print("Saíndo do programa.")
                break
            else:
                print("Erro: Opción non válida. Por favor, elixe unha opción do menú.")
        except ValueError as e:
            print(f"Erro: {e}")

if __name__ == "__main__":
    main()