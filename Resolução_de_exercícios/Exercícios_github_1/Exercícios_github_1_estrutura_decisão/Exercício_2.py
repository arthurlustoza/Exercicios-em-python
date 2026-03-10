"""
Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo. Caso seja igual a 0, retorne None.
"""

num_1 = int(input("Digite o numero para verificar se e negativo o positivo: "))

if num_1 > 0:
    print("Número e positivo ")
elif num_1 < 0:
    print("Número e negativo ")
else:
    print("None")
