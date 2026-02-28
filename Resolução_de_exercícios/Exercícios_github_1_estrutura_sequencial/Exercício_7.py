#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário. 
# Mostrar a área com 2 casas decimais.

print("Descubra a área de um quadrado X2")

lado = float(input('Digite o lado do quadrado:'))

area = lado ** 2

print(f"A sua area e de:{area:.1f}")

areax2 = area * 2

print(f"Sua área x 2 e de:{areax2:.2f}")


