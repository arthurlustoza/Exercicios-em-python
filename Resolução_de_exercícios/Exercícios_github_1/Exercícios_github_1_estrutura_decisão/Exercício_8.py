"""
Exercício 08 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão
é sempre pelo mais barato.
Mostrar o resultado com duas casas decimais

    >>> decidir_melhor_produto(2, 3, 5)
    Melhor produto custa R$ 2.00
    >>> decidir_melhor_produto(10, 5.55, 7)
    Melhor produto custa R$ 5.55
    >>> decidir_melhor_produto(20, 30, 17.62)
    Melhor produto custa R$ 17.62
    >>> decidir_melhor_produto(7, 1, 15)
    Melhor produto custa R$ 1.00

"""

produto_1 = float(input("Digite o preço do produto 1: "))
produto_2 = float(input("Digite o preço do produto 2: "))
produto_3 = float(input("Digite o preço do produto 3: "))

mais_barato = produto_1

if produto_2 < mais_barato:
    mais_barato = produto_2

if produto_3 < mais_barato:
    mais_barato = produto_3

print(f"Melhor produto: {mais_barato:.2f}")
