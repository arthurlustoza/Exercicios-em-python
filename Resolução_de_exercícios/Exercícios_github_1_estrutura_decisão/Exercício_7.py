"""
Faça um Programa que leia três números e mostre o maior e o menor deles.
"""

num_1 = float(input("Digite o primeiro número: "))
num_2 = float(input("Digite o segundo número: "))
num_3 = float(input("Digite o terceiro número: "))

maior_num = num_1

if num_2 > maior_num:
    maior_num = num_2

if num_3 > maior_num:
    maior_num = num_3


menor_num = num_1

if num_2 < menor_num:
    menor_num = num_2

if num_3 < menor_num:
    menor_num = num_3

print(f"O maior número e: {maior_num}")
print(f"O menor número e: {menor_num}")
