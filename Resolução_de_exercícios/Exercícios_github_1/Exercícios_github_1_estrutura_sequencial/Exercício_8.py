'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.
Mostrar salário com duas casas decimais
'''

ganho_porHora = float(input('Quanto você ganha por hora: '))

horas_trabalhadas = float(input('Quantas horas você trabalhou por Mês: '))

salario_finalMes = ganho_porHora * horas_trabalhadas

print(f"Seu salario no final de mês e de: R$ {salario_finalMes:.2f}")

