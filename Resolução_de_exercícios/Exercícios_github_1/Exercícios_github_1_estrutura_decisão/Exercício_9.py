"""
Exercício 09 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que leia três números e mostre-os em ordem decrescente.

    >>> ordenar_decrescente(2, 3, 5)
    5, 3, 2
    >>> ordenar_decrescente(10, 5.55, 7)
    10, 7, 5.55
    >>> ordenar_decrescente(20, 30, 17.62)
    30, 20, 17.62
    >>> ordenar_decrescente(7, 1, 15)
    15, 7, 1
"""

num_1 = float(input("Digite o primeiro 1: "))
num_2 = float(input("Digite o segundo 2: "))
num_3 = float(input("Digite o terceiro 3: "))


# Descobrir o maior número
ordem_1 = num_1

if num_2 > ordem_1:
    ordem_1 = num_2

if num_3 > ordem_1:
    ordem_1 = num_3


# Descobrir o menor número
ordem_3 = num_1

if num_2 < ordem_3:
    ordem_2 = num_2

if num_3 < ordem_3:
    ordem_2 = num_3


ordem_2 = num_1

if ordem_2 > num_2 and ordem_2 < num_3:
    ordem_2 = num_1


print(ordem_1, ordem_2, ordem_3)


# corrigido
