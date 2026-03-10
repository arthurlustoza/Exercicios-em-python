"""
Exercício 24 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da
operação deve ser acompanhado de uma frase que diga se o número é:
  par ou ímpar;
  positivo ou negativo;
  inteiro ou decimal.

Mostre o restultado com duas casas decimais

    >>> fazer_operacao_e_classificar(2, 3, '+')
    Resultado: 5.00
    Número é impar, positivo e inteiro.
    >>> fazer_operacao_e_classificar(-4, 2, '/')
    Resultado: -2.00
    Número é par, negativo e inteiro.
    >>> fazer_operacao_e_classificar(0, 2, '*')
    Resultado: 0.00
    Número é par, neutro e inteiro.
    >>> fazer_operacao_e_classificar(-3.14, 2, '*')
    Resultado: -6.28
    Número é negativo e decimal.
    >>> fazer_operacao_e_classificar(3.14, 2, '-')
    Resultado: 1.14
    Número é positivo e decimal.

"""

print("Calculadora!")

num_1 = int(input("Digite o primeiro número para a operação:"))
num_2 = int(input("Digite o segundo número para operação: "))

operacao = str(input("Digite a operação desejada: "))


# Escolha de operação
if operacao == "+":
    resultado = num_1 + num_2
elif operacao == "-":
    resultado = num_1 - num_2
elif operacao == "/":
    resultado = num_1 / num_2
elif operacao == "*":
    resultado = num_1 * num_2
else:
    print("Operação invalida")

verficar_par_impar = resultado % 2

# Verificar par ou ímpar
if verficar_par_impar == 0:
    print("Par")
else:
    print("ìmpar")

# Verificar se o resultado e negativo ou positivo
if resultado >= 0:
    print("Positivo")
else:
    print("Negativo")

if resultado % 1 == 0:
    print("Inteiro")
else:
    print("Decimal")

print(f"Resultado: {resultado:.2f}")
