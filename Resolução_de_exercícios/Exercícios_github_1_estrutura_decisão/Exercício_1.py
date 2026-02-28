"""
Faça um Programa que peça dois números e imprima o maior deles.
"""

num_1, num_2 = int(input("Digite o primeiro número: ")), int(
    input("Digite o segundo número: ")
)

if num_1 > num_2:
    print(f"O primeiro número {num_1:.0f} e maior")
else:
    print(f"O segundo número {num_2:.0f} e maior")
