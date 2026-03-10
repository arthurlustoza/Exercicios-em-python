"""
Exercício 28 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há
limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um
desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo
usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total,
tipo de pagamento, valor do desconto e valor a pagar.

Mostre o restultado com duas casas decimais

    >>> calcular_preco_da_carne('Filé Duplo', 2, 'dinheiro')
    '2 kg de Filé Duplo a R$ 4.90/kg saem a R$ 9.80. Não há desconto, pagamento feito com dinheiro'
    >>> calcular_preco_da_carne('Filé Duplo', 4, 'cartão tabajara')
    '4 kg de Filé Duplo a R$ 4.90/kg saem a R$ 19.60. Com desconto de 5% pelo pagamento feito com cartão tabajara, fica R$ 18.62'
    >>> calcular_preco_da_carne('Filé Duplo', 6, 'pix')
    '6 kg de Filé Duplo a R$ 5.80/kg saem a R$ 34.80. Não há desconto, pagamento feito com pix'
    >>> calcular_preco_da_carne('Filé Duplo', 8, 'cartão tabajara')
    '8 kg de Filé Duplo a R$ 5.80/kg saem a R$ 46.40. Com desconto de 5% pelo pagamento feito com cartão tabajara, fica R$ 44.08'
    >>> calcular_preco_da_carne('Alcatra', 2, 'dinheiro')
    '2 kg de Alcatra a R$ 5.90/kg saem a R$ 11.80. Não há desconto, pagamento feito com dinheiro'
    >>> calcular_preco_da_carne('Alcatra', 4, 'cartão tabajara')
    '4 kg de Alcatra a R$ 5.90/kg saem a R$ 23.60. Com desconto de 5% pelo pagamento feito com cartão tabajara, fica R$ 22.42'
    >>> calcular_preco_da_carne('Alcatra', 6, 'dinheiro')
    '6 kg de Alcatra a R$ 6.80/kg saem a R$ 40.80. Não há desconto, pagamento feito com dinheiro'
    >>> calcular_preco_da_carne('Alcatra', 8, 'cartão tabajara')
    '8 kg de Alcatra a R$ 6.80/kg saem a R$ 54.40. Com desconto de 5% pelo pagamento feito com cartão tabajara, fica R$ 51.68'
    >>> calcular_preco_da_carne('Picanha', 2, 'dinheiro')
    '2 kg de Picanha a R$ 6.90/kg saem a R$ 13.80. Não há desconto, pagamento feito com dinheiro'
    >>> calcular_preco_da_carne('Picanha', 4, 'cartão tabajara')
    '4 kg de Picanha a R$ 6.90/kg saem a R$ 27.60. Com desconto de 5% pelo pagamento feito com cartão tabajara, fica R$ 26.22'
    >>> calcular_preco_da_carne('Picanha', 6, 'dinheiro')
    '6 kg de Picanha a R$ 7.80/kg saem a R$ 46.80. Não há desconto, pagamento feito com dinheiro'
    >>> calcular_preco_da_carne('Picanha', 8, 'cartão tabajara')
    '8 kg de Picanha a R$ 7.80/kg saem a R$ 62.40. Com desconto de 5% pelo pagamento feito com cartão tabajara, fica R$ 59.28'

"""

print("Hipermercado promoção")

tipo_carne = str(input("Qual tipo de carne deseja levar: ")).lower().strip()
quantidade_carne = float(input("Quantidade da carne por kilo: "))

print("Atenção: Aceitamos Cartão Tabajara, Pix e Dinheiro")
tipo_pagamento = str(input("Informe o tipo de pagamento: ")).lower().strip()

# Preço por kilo File
if tipo_carne == "file":
    if quantidade_carne <= 5:
        preco_por_kilo = 4.90
    else:
        preco_por_kilo = 5.80

# Preço por kilo Alcatra
elif tipo_carne == "alcatra":
    if quantidade_carne <= 5:
        preco_por_kilo = 5.90
    else:
        preco_por_kilo = 6.80

# Preço por kilo Picanha
elif tipo_carne == "picanha":
    if quantidade_carne <= 5:
        preco_por_kilo = 6.90
    else:
        preco_por_kilo = 7.80


# Conta para somar o total da mercadoria
valor_total_mercadoria = quantidade_carne * preco_por_kilo


# desconto
if tipo_pagamento == "cartao tabajara":
    porcentagem = 5
    fator_desconto = porcentagem / 100
    valor_desconto = valor_total_mercadoria * fator_desconto
    mercadoria_total_desconto = valor_total_mercadoria - valor_desconto
    desconto_texto = str(
        f"Com desconto de {porcentagem}% pelo pagamento feito com o cartão tabajara, fica R${mercadoria_total_desconto:.2f}"
    )
else:

    porcentagem = 0
    fator_desconto = porcentagem / 100
    valor_desconto = valor_total_mercadoria * fator_desconto
    desconto_texto = str(f"Não há desconto, pagamento feito com {tipo_pagamento}")
    mercadoria_total_desconto = valor_total_mercadoria - valor_desconto


print("Cupom Fiscal")

print(
    f"{quantidade_carne} kg de {tipo_carne} a R${preco_por_kilo:.2f}/KG saem a R${valor_total_mercadoria:.2f}.{desconto_texto}"
)
