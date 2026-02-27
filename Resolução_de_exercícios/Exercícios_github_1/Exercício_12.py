"""
Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte
fórmula: (72.7*altura) - 58
Mostrar a área com 1 casa decimal.
"""

print("Calculando IMC")

formula = float(72.7)

altura = float(input("Digite sua altura: "))

peso_ideal = (formula * altura) - 58

print(f"Seu peso ideal e de: {peso_ideal:.1f}")
