"""
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de
São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá
pagar.
Imprima os dados do programa com as mensagens adequadas.
Mostrar o peso e multa com duas casas decimais
"""

print("Calculadora de Multa!")

peixes_emKG = float(input("Digite a quantidade em KG de peixes:"))

excesso = peixes_emKG - 50

print(f"Excesso em Kg: {excesso:.2f}")

multa = excesso * 4

print(f"A sua multa vai ser de: R${multa:.2f}")
