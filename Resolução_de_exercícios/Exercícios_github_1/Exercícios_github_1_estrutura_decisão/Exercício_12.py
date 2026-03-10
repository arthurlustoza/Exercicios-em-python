"""
Exercício 12 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que
depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do
Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos
os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
  Salário Bruto até 900 (inclusive) - isento
  Salário Bruto até 1500 (inclusive) - desconto de 5%
  Salário Bruto até 2500 (inclusive) - desconto de 10%
  Salário Bruto acima de 2500 - desconto de 20%

Mostrar valores monetários com duas casas decimais, alinhados à direita, com espaço para 5 dígitos de salário, ou seja,
até R$ 99999,99

    >>> calcular_salario_liquido(1, 160)
    Salário Bruto: (R$ 1.00 * 160)     : R$   160.00
    (-) IR (0%)                        : R$     0.00
    (-) INSS (10%)                     : R$    16.00
    (-) Sindicato (3%)                 : R$     4.80
    FGTS (11%)                         : R$    17.60
    Total de descontos                 : R$    20.80
    Salário Liquido                    : R$   139.20
    >>> calcular_salario_liquido(5, 220)
    Salário Bruto: (R$ 5.00 * 220)     : R$  1100.00
    (-) IR (5%)                        : R$    55.00
    (-) INSS (10%)                     : R$   110.00
    (-) Sindicato (3%)                 : R$    33.00
    FGTS (11%)                         : R$   121.00
    Total de descontos                 : R$   198.00
    Salário Liquido                    : R$   902.00
    >>> calcular_salario_liquido(10, 160)
    Salário Bruto: (R$ 10.00 * 160)    : R$  1600.00
    (-) IR (10%)                       : R$   160.00
    (-) INSS (10%)                     : R$   160.00
    (-) Sindicato (3%)                 : R$    48.00
    FGTS (11%)                         : R$   176.00
    Total de descontos                 : R$   368.00
    Salário Liquido                    : R$  1232.00
    >>> calcular_salario_liquido(100, 160)
    Salário Bruto: (R$ 100.00 * 160)   : R$ 16000.00
    (-) IR (20%)                       : R$  3200.00
    (-) INSS (10%)                     : R$  1600.00
    (-) Sindicato (3%)                 : R$   480.00
    FGTS (11%)                         : R$  1760.00
    Total de descontos                 : R$  5280.00
    Salário Liquido                    : R$ 10720.00

"""

print("Calculadora de Impostos")

valor_hora = float(
    input("Valor da sua hora: ")
)  # float ao inves de int pois se o valor for 5:50 o valor quebra!

horas_trabalhadas = int(input("Quantidade de horas trabalhadas: "))

salario_bruto = valor_hora * horas_trabalhadas

# estrutura para definir a % do imposto que será aplicado
if salario_bruto <= 900:
    imposto_de_renda = 0
elif salario_bruto <= 1500:
    imposto_de_renda = 5
elif salario_bruto <= 2500:
    imposto_de_renda = 10
else:
    imposto_de_renda = 20


# Imprime salário bruto
print(
    f"Salário Bruto: ({valor_hora:.2f} * {horas_trabalhadas:.2f})  : R$  {salario_bruto:.2f}"
)

# aliquota da conta para calcular o valor do imposto de renda
aliquota = (
    imposto_de_renda / 100
)  # Alíquota é o percentual ou valor fixo estabelecido em lei para calcular a quantia de um imposto.

# Calculo imposto de renda mais a impressao
valor_imposto_de_renda = salario_bruto * aliquota
print(f"IR ({imposto_de_renda}%):  R$ {valor_imposto_de_renda:.1f}")

# Calculo do INSS e impressao
valor_inss = salario_bruto * 0.1
print(f"INSS (10%):  R$ {valor_inss:.1f}")

# Calculo do Sindicato e impressao
valor_sindicato = salario_bruto * 0.03
print(f"Sindicado (3%):   R$  {valor_sindicato:.1f}")

# Calculo FGTS e impressao
valor_fgts = salario_bruto * 0.11
print(f"FGTS (11%):   R$  {valor_fgts:.1f}")

# calculos finais
salario_liquido = salario_bruto - valor_imposto_de_renda - valor_inss - valor_sindicato

total_descontos = (
    valor_imposto_de_renda + valor_inss + valor_sindicato
)  # pode so calcular todos os descontos

print(f"Total de descontos:  R$  {total_descontos:.2f}")


print(f"Salario Liquido:  R$  {salario_liquido:.2f}")
