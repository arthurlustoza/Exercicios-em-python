"""
Exercício 26 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Um posto está vendendo combustíveis com a seguinte tabela de descontos:

    Álcool:
    até 20 litros, desconto de 3% por litro
    acima de 20 litros, desconto de 5% por litro
    Gasolina:
    até 20 litros, desconto de 4% por litro
    acima de 20 litros, desconto de 6% por litro
Escreva um algoritmo que leia o número de litros vendidos,
o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o
preço do litro do álcool é R$ 1,90.

Mostre o restultado com duas casas decimais

    >>> calcular_abastecimento(10, 'A')
    '10 litro(s) de álcool custa(m): R$ 19.00. Com 3% de desconto, fica R$ 18.43'
    >>> calcular_abastecimento(20, 'A')
    '20 litro(s) de álcool custa(m): R$ 38.00. Com 3% de desconto, fica R$ 36.86'
    >>> calcular_abastecimento(30, 'A')
    '30 litro(s) de álcool custa(m): R$ 57.00. Com 5% de desconto, fica R$ 54.15'
    >>> calcular_abastecimento(10, 'G')
    '10 litro(s) de gasolina custa(m): R$ 25.00. Com 4% de desconto, fica R$ 24.00'
    >>> calcular_abastecimento(20, 'G')
    '20 litro(s) de gasolina custa(m): R$ 50.00. Com 4% de desconto, fica R$ 48.00'
    >>> calcular_abastecimento(30, 'G')
    '30 litro(s) de gasolina custa(m): R$ 75.00. Com 6% de desconto, fica R$ 70.50'

"""

print("Posto de Gasolina!")

combustivel = (
    str(input("Digite a sigla do combustivel, (A) = alcool, (G) = gasolina: "))
    .lower()
    .strip()
)
porcentagem = int(0)
preco_litro_alcool = float(1.90)
preco_litro_gasolina = float(2.50)


if combustivel == "a":
    print("Alcool")
    litros_alcool = float(input("Digite a quantidade de combustivel: "))

    if litros_alcool <= 20:
        preco_final_alcool = litros_alcool * preco_litro_alcool
        porcentagem = 3
        fator_desconto = porcentagem / 100
        valor_desconto = preco_final_alcool * fator_desconto
        preco_alcool_final_desconto = preco_final_alcool - valor_desconto

        print(
            f"{litros_alcool} litro(s) de alcool custa(m): R${preco_final_alcool:.1f}. Com {porcentagem}% de desconto, fica R$ {preco_alcool_final_desconto}"
        )
    elif litros_alcool > 20:
        preco_final_alcool = litros_alcool * preco_litro_alcool
        porcentagem = 5
        fator_desconto = porcentagem / 100
        valor_desconto = preco_final_alcool * fator_desconto
        preco_alcool_final_desconto = preco_final_alcool - valor_desconto

        print(
            f"{litros_alcool} litro(s) de alcool custa(m): R${preco_final_alcool:.1f}. Com {porcentagem}% de desconto, fica R$ {preco_alcool_final_desconto}"
        )


elif combustivel == "g":
    print("Gasolina")
    litros_gasolina = float(input("Digite a quantidade de gasolina: "))

    if litros_gasolina <= 20:
        preco_final_gasolina = litros_gasolina * preco_litro_gasolina
        porcentagem = 4
        fator_desconto = porcentagem / 100
        valor_desconto = preco_final_gasolina * fator_desconto
        preco_gasolina_final_desconto = preco_final_gasolina - valor_desconto

        print(
            f"{litros_gasolina} litro(s) de alcool custa(m): R${preco_final_gasolina:.1f}. Com {porcentagem}% de desconto, fica R$ {preco_gasolina_final_desconto}"
        )
    elif litros_gasolina > 20:
        preco_final_gasolina = litros_gasolina * preco_litro_gasolina
        porcentagem = 6
        fator_desconto = porcentagem / 100
        valor_desconto = preco_final_gasolina * fator_desconto
        preco_gasolina_final_desconto = preco_final_gasolina - valor_desconto

        print(
            f"{litros_gasolina} litro(s) de alcool custa(m): R${preco_final_gasolina:.1f}. Com {porcentagem}% de desconto, fica R$ {preco_gasolina_final_desconto}"
        )
else:
    print("Invalido")
    exit()
