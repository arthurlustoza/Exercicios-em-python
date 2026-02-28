"""
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
Mostrar a área com 1 casa decimal.
"""

print("Calculadora de Peso ideal para h e m")

altura = float(input("Digite a sua altura: "))

alturaP_homens = (72.7 * altura) - 58
alturaP_mulheres = (62.1 * altura) - 58

print(f"Seu peso ideal é {alturaP_homens:.1f} se você for Homem")
print(f"Seu peso ideal é {alturaP_mulheres:.1f} se você for mulher")
