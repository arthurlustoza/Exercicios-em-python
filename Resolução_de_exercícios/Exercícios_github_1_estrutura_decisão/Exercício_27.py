"""
Exercício 27 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Uma fruteira está vendendo frutas com a seguinte tabela de preços:

                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
receberá ainda um desconto de 10% sobre este total.
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o
valor a ser pago pelo cliente.
Mostre o restultado com duas casas decimais

    >>> calcular_preco_da_compra(2, 0)
    (+)  Morango  - valor:  R$  5.00 - quantidade:  2 kg - preço: R$ 2.50/kg
    (-)  Desconto - valor:  R$  0.00
              Valor Total:  R$  5.00
    >>> calcular_preco_da_compra(6, 0)
    (+)  Morango  - valor:  R$ 13.20 - quantidade:  6 kg - preço: R$ 2.20/kg
    (-)  Desconto - valor:  R$  0.00
              Valor Total:  R$ 13.20
    >>> calcular_preco_da_compra(9, 0)
    (+)  Morango  - valor:  R$ 19.80 - quantidade:  9 kg - preço: R$ 2.20/kg
    (-)  Desconto - valor:  R$  1.98
              Valor Total:  R$ 17.82
    >>> calcular_preco_da_compra(0, 2)
    (+)  Maça     - valor:  R$  3.60 - quantidade:  2 kg - preço: R$ 1.80/kg
    (-)  Desconto - valor:  R$  0.00
              Valor Total:  R$  3.60
    >>> calcular_preco_da_compra(0, 6)
    (+)  Maça     - valor:  R$  9.00 - quantidade:  6 kg - preço: R$ 1.50/kg
    (-)  Desconto - valor:  R$  0.00
              Valor Total:  R$  9.00
    >>> calcular_preco_da_compra(0, 9)
    (+)  Maça     - valor:  R$ 13.50 - quantidade:  9 kg - preço: R$ 1.50/kg
    (-)  Desconto - valor:  R$  1.35
              Valor Total:  R$ 12.15
    >>> calcular_preco_da_compra(2, 2)
    (+)  Morango  - valor:  R$  5.00 - quantidade:  2 kg - preço: R$ 2.50/kg
    (+)  Maça     - valor:  R$  3.60 - quantidade:  2 kg - preço: R$ 1.80/kg
    (-)  Desconto - valor:  R$  0.00
              Valor Total:  R$  8.60
    >>> calcular_preco_da_compra(7, 2)
    (+)  Morango  - valor:  R$ 15.40 - quantidade:  7 kg - preço: R$ 2.20/kg
    (+)  Maça     - valor:  R$  3.60 - quantidade:  2 kg - preço: R$ 1.80/kg
    (-)  Desconto - valor:  R$  1.90
              Valor Total:  R$ 17.10
    >>> calcular_preco_da_compra(7, 7)
    (+)  Morango  - valor:  R$ 15.40 - quantidade:  7 kg - preço: R$ 2.20/kg
    (+)  Maça     - valor:  R$ 10.50 - quantidade:  7 kg - preço: R$ 1.50/kg
    (-)  Desconto - valor:  R$  2.59
              Valor Total:  R$ 23.31
"""

print("Frutaria")


kilos_para_levar_morango = float(
    input("Digite quantos kilos de morango deseja levar: ")
)

kilos_para_levar_maca = float(input("Digite quantos kilos de maca deseja levar: "))

if kilos_para_levar_morango <= 5:
    valor_kilo_morango = 2.50
else:
    valor_kilo_morango = 2.20

if kilos_para_levar_maca <= 5:
    valor_kilo_maca = 1.80
else:
    valor_kilo_maca = 1.50

mercadoria_valor_morango = kilos_para_levar_morango * valor_kilo_morango
mercadoira_valor_maca = kilos_para_levar_maca * valor_kilo_maca

valor_total_kilo = kilos_para_levar_morango + kilos_para_levar_maca
valor_total_mercadoria = mercadoria_valor_morango + mercadoira_valor_maca

if valor_total_kilo > 8 or valor_total_mercadoria > 25:
    porcentagem = 10
    fator_desconto = porcentagem / 100
    valor_desconto = valor_total_mercadoria * fator_desconto
    mercadoria_total_desconto = valor_total_mercadoria - valor_desconto
else:
    porcentagem = 0
    fator_desconto = porcentagem / 100
    valor_desconto = valor_total_mercadoria * fator_desconto
    mercadoria_total_desconto = valor_total_mercadoria - valor_desconto


if kilos_para_levar_morango == 0:
    print(
        f"(+) Maça  - valor: R${mercadoira_valor_maca:.2f} - quantidade: {kilos_para_levar_maca}KG  - valor/kilo: R${valor_kilo_maca:.2f}"
    )


elif kilos_para_levar_maca == 0:
    print(
        f"(+) Morango  - valor: R${mercadoria_valor_morango:.2f} - quantidade: {kilos_para_levar_morango}KG  - valor/kilo: R${valor_kilo_morango:.2f}"
    )

else:
    print(
        f"(+) Maça  - valor: R${mercadoira_valor_maca:.2f} - quantidade: {kilos_para_levar_maca}KG  - valor/kilo: R${valor_kilo_maca:.2f}"
    )
    print(
        f"(+) Morango  - valor: R${mercadoria_valor_morango:.2f} - quantidade: {kilos_para_levar_morango}KG  - valor/kilo: R${valor_kilo_morango:.2f}"
    )


print(f"(-) Desconto - valor: R${valor_desconto:.2f}")

print(f"Valor total: R$ {mercadoria_total_desconto:.2f}")
