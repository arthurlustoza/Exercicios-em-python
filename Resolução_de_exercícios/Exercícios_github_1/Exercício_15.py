"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido
Mostrar os resultados com duas casas decimais
"""

print("Salarío/c Descontos")

ganhos_por_hora = float(input("Digite quanto você ganha por hora: "))
horas_trabalhadas = float(input("Digite números de horas trabalhadas por mês: "))

salario_mes_bruto = ganhos_por_hora * horas_trabalhadas

print(f"Salário Bruto por mês: {salario_mes_bruto:.2f}")

imposto_renda = salario_mes_bruto * 0.11

inss = salario_mes_bruto * 0.08

sindicado = salario_mes_bruto * 0.05

salario_mes_liquido = salario_mes_bruto - imposto_renda - inss - sindicado

print(f"Salário por mês Liquido: {salario_mes_liquido:.2f}")
