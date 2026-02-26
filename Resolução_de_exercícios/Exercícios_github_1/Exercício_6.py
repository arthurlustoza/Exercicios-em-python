#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área. Mostrar a área com 4 casas decimais.
print("Descubra a área do círculo")
r = float(input('Digite o raio do círculo:'))

pi = 3.1415

area = pi * r  ** 2

print(f"A área desejada e: {area:.4f}")

