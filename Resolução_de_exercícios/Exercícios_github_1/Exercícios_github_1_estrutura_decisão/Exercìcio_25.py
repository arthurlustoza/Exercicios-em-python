"""
Exercício 25 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

  "Telefonou para a vítima?"
  "Esteve no local do crime?"
  "Mora perto da vítima?"
  "Devia para a vítima?"
  "Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeito",
entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".

    >>> investigar('Sim','Sim','Sim','Sim','Sim')
    'Assassino'
    >>> investigar('Sim','Sim','Sim','Sim','Não')
    'Cúmplice'
    >>> investigar('Sim','Sim','Sim','Não','Não')
    'Cúmplice'
    >>> investigar('Sim','Sim','Não','Não','Não')
    'Suspeito'
    >>> investigar('Sim','Não','Não','Não','Não')
    'Inocente'
    >>> investigar('Não','Não','Não','Não','Não')
    'Inocente'

"""

print("Deteive o game")

telefone_vitima = str(input("Telefonou para a vítima ?")).lower().strip()
local_crime = str(input("Esteve no local do crime ? ")).lower().strip()
mora_perto = str(input("Mora perto da vítima? ")).lower().strip()
divida_vitima = str(input("Devia a vitima: ")).lower().strip()
ja_trabalhou = str(input("Já trabalhou com a vítima? ")).lower().strip()

quantidade_sim = 0
quantidade_nao = 0

# contador de quantidade de sim e nao
if telefone_vitima == "sim":
    quantidade_sim += 1
else:
    quantidade_nao += 1

if local_crime == "sim":
    quantidade_sim += 1
else:
    quantidade_nao += 1

if mora_perto == "sim":
    quantidade_sim += 1
else:
    quantidade_nao += 1

if ja_trabalhou == "sim":
    quantidade_sim += 1
else:
    quantidade_nao += 1

if divida_vitima == "sim":
    quantidade_sim += 1
else:
    quantidade_nao += 1

# verificacao de pena
if quantidade_sim == 2:
    print("Suspeito")
elif quantidade_sim == 4 or quantidade_sim == 3:
    print("Cúmplice")
elif quantidade_sim == 5:
    print("Assasino!")
else:
    print("Inocente")


print(f"Quantidade de sim: {quantidade_sim}, Quantidade de não: {quantidade_nao}")
