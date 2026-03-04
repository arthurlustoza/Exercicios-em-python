"""
Exercício 13 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.),
se digitar outro valor deve aparecer valor inválido.

    >>> calcular_dia_da_semana(1)
    'Domingo'
    >>> calcular_dia_da_semana(2)
    'Segunda'
    >>> calcular_dia_da_semana(3)
    'Terça'
    >>> calcular_dia_da_semana(4)
    'Quarta'
    >>> calcular_dia_da_semana(5)
    'Quinta'
    >>> calcular_dia_da_semana(6)
    'Sexta'
    >>> calcular_dia_da_semana(7)
    'Sábado'
    >>> calcular_dia_da_semana(8)
    'Dia Inválido'
    >>> calcular_dia_da_semana(0)
    'Dia Inválido'

"""

print("A partir do número saber o dai da semana!")

dia_da_semana = int(input("Digite o número de 1 a 7: "))

if dia_da_semana == 1:
    print("DOMINGO")
elif dia_da_semana == 2:
    print("SEGUNDA")
elif dia_da_semana == 3:
    print("TERÇA")
elif dia_da_semana == 4:
    print("QUARTA")
elif dia_da_semana == 5:
    print("QUINTA")
elif dia_da_semana == 6:
    print("SEXTA")
elif dia_da_semana == 7:
    print("SABADO")
elif dia_da_semana < 1 or dia_da_semana > 7:
    print("Número invalido")
