"""
Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
 - A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
 - A mensagem "Reprovado", se a média for menor do que sete;
 - A mensagem "Aprovado com Distinção", se a média for igual a dez.
Obs: 0 <= nota <= 10
"""

nota_1 = float(input("Digite a nota do 1 semestre: "))
nota_2 = float(input("Digite a nota do 2 semestre: "))

media = (nota_1 + nota_2) / 2

if media >= 7 and media <= 9:
    print("Parabens! Você foi aprovado")
elif media <= 6:
    print("Você foi reprovado !")
else:
    print("Aprovado com Distinção")

print(
    f" Sua media e de: {media:.1f}| Nota 1 Semestre: {nota_1:.1f}| Nota 2 Semestre: {nota_2:.1f}"
)
