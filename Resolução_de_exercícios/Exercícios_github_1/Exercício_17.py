"""
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e
que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o custo seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
"""

import math

print("Loja de Tintas!")

tamanho_area_M2 = int(input("Digite o tamanho da área a ser pintada em M2: "))

litros_usados = tamanho_area_M2 * 6

lata_de_tinta = math.ceil(litros_usados / 18)

preco_lata = lata_de_tinta * 80

print(f"Quantidade de litros de tinta: {litros_usados:.1f}")
print(
    f"Quantidade de latas e preço: {lata_de_tinta} latas de tinta saem por: R$ {preco_lata:.1f}"
)
