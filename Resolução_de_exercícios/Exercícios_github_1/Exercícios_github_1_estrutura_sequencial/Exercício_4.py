#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

print("Descubra a sua média!")

bimestres = 4

bim1  = int(input('Sua nota do 1 bim: '))
bim2  = int(input('Sua nota do 2 bim: '))
bim3  = int(input('Sua nota do 3 bim: '))
bim4  = int(input('Sua nota do 4 bim: '))

resultado = (bim1 + bim2 + bim3 + bim4) / bimestres

print("A sua média e de:", resultado)