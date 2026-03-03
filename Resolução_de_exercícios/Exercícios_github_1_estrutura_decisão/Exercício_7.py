"""
Faça um Programa que leia três números e mostre o maior e o menor deles.
"""

num_1 = int(input("Digite o primeiro número: "))
num_2 = int(input("Digite o segundo número: "))
num_3 = int(input("Digite o terceiro número: "))


if num_1 > num_2 and num_1 > num_3:
    print(f"Maior:{num_1}")
elif num_2 > num_1 and num_2 > num_3:
    print(f"Maior:{num_2}")
elif num_3 > num_1 and num_3 > num_2:
    print(f"Maior:{num_3}")
else:
    print("Número iguais não podem ser comparados !")

num_4 = num_1  # Recebe o valor de 1 para a outra comparação!
num_5 = num_2  # Recebe o valor de 2 para a outra comparação!
num_6 = num_3  # Recebe o valor de 3 para a outra comparação!

if num_4 < num_5 and num_4 < num_6:
    print(f"Menor:{num_4}")
elif num_5 < num_4 and num_5 < num_6:
    print(f"Menor:{num_5}")
elif num_6 < num_4 and num_6 < num_5:
    print(f"Menor:{num_6}")
else:
    print("Números iguais não podem ser comparados!")
