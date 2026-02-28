"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
 1) o produto do dobro do primeiro com metade do segundo;
 2) a soma do triplo do primeiro com o terceiro;
 3) o terceiro elevado ao cubo.
"""

print("Math!")

num_1, num_2 = int(input("Digite o primeiro número inteiro: ")), int(
    input("Digite o segundo número inteiro: ")
)

num_r3 = float(input("Digite um número real: "))

resultado_1 = (num_1 * 2) * (num_2 / 2)

print(f"Resutado da 1 equação: {resultado_1:.0f}")

resultado_2 = (num_1 * 3) + num_r3

print(f"Resultado da 2 equação: {resultado_2:.1f}")

resultado_3 = num_r3**3

print(f"Resultado da terceira equação: {resultado_3:.1f}")
