"""
Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Retorne: F - Feminino ou M - Masculino. Para quaisquer outros valores, retorne Sexo Inválido.
"""

genero = str(input("Digite seu gênero 'masculino' - (M) ou 'Feminino' - (F): "))

if genero == "M":
    print("M  - Masculino ")
elif genero == "F":
    print("F - Feminino")
else:
    print("Gênero não reconhecido")
