"""
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""

print("Verificando se e vogal ou consoante")

letra = str(input("Digite a letra desejada: ").lower())

vogal = "aeiou"

if letra in vogal:
    print("Vogal")
else:
    print("Consoante")
