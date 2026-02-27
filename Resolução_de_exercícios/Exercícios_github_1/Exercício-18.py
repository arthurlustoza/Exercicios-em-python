"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
Arredonde o tempo em minutos
"""

import math

print("Calculadora de tempo de download !")

tamanho_arquivoMB = int(input("Digite o tamanho do arquivo em MB: "))

velocidade_internet = int(input("Digite a velocidade da sua internet: "))

tempo_segundos = (tamanho_arquivoMB * 8) / velocidade_internet

tempo_minutos = math.ceil(tempo_segundos / 60)


print(f"O tempo estimado de download e de: {tempo_minutos:.1f} minutos")
