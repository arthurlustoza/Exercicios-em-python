"""
Faça um programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de
18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""

import math

print("Loja de tintas")

tamanho_M2 = float(input("Digite o tamanho em M2 da área a ser pintada: "))

rendimento_tinta = math.ceil(tamanho_M2 / 3)

print(f"Quantidade de litros de tinta nescessaria: {rendimento_tinta:.0f}L")

lata = math.ceil(rendimento_tinta / 18)

preco_final = lata * 80

print(f"Quantidade de Latas sescessarias:{lata}")
print(f"Preço final:R${preco_final:.0f}")
