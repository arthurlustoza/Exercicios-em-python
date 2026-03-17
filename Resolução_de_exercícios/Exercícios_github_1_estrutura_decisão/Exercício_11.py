"""
Exercício 11 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
  salários até R$ 280,00 (incluindo) : aumento de 20%
  salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
  salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
  salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
  o salário antes do reajuste;
  o percentual de aumento aplicado;
  o valor do aumento;
  o novo salário, após o aumento.

Mostrar valores monetários com duas casas decimais.

    >>> calcular_aumento(100)
    Salário atual: R$ 100.00
    Aumento porcentual: 20%
    Valor do aumento: R$ 20.00
    Novo salário: R$ 120.00
    >>> calcular_aumento(300)
    Salário atual: R$ 300.00
    Aumento porcentual: 15%
    Valor do aumento: R$ 45.00
    Novo salário: R$ 345.00
    >>> calcular_aumento(800)
    Salário atual: R$ 800.00
    Aumento porcentual: 10%
    Valor do aumento: R$ 80.00
    Novo salário: R$ 880.00
    >>> calcular_aumento(1600)
    Salário atual: R$ 1600.00
    Aumento porcentual: 5%
    Valor do aumento: R$ 80.00
    Novo salário: R$ 1680.00
"""

print("Calculadora de Salário !")

salario_bruto = float(input("Digite o seu salarío para o reajuste: "))

print(f"Salario bruto e de: {salario_bruto:.2f} R$")

if salario_bruto <= 280:
    salario_com_aumento = salario_bruto * 1.20
    print("Aumento de 20%")
elif salario_bruto > 280 and salario_bruto <= 700:
    salario_com_aumento = salario_bruto * 1.15
    print("Aumento de 15%")
elif salario_bruto > 700 and salario_bruto == 1500:
    salario_com_aumento = salario_bruto * 1.10
    print("Aumento de 10%")
else:
    salario_com_aumento = salario_bruto * 1.05
    print("Aumento de 5%")

print(f"Salario com aumento: {salario_com_aumento:.2f} R$")

aumento = salario_com_aumento - salario_bruto
print(f"Aumento foi de: {aumento:.2f} R$")
