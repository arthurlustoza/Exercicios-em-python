"""
Exercício 15 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;

    >>> classificar_triangulo(2, 3, 4)
    'Triângulo Escaleno'
    >>> classificar_triangulo(2, 2, 3)
    'Triângulo Isósceles'
    >>> classificar_triangulo(2, 2, 2)
    'Triângulo Equilátero'
    >>> classificar_triangulo(2, 2, 5)
    'Não é um triângulo'
    >>> classificar_triangulo(5, 2, 2)
    'Não é um triângulo'
    >>> classificar_triangulo(2, 5, 2)
    'Não é um triângulo'

"""

print("Descobra o tipo de Triângulo!")

lado_1 = int(input("Digite o lado 1 do triângulo: "))
lado_2 = int(input("Digite o lado 2 do triângulo: "))
lado_3 = int(input("Digite o lado 3 do triângulo: "))

if lado_1 + lado_2 > lado_3:
    if lado_1 == lado_2 == lado_3:
        print("Triângulo Equilátero")
    elif lado_1 != lado_2 != lado_3:
        print("Triângulo Escaleno")
    elif (
        lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3
    ):  # Precisei de ajuda com a lógica dessa parte!
        print("Triângulo Isósceles")
else:
    print("Não e um triângulo")
