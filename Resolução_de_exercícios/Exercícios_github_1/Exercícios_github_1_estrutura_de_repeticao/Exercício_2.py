"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma
mensagem de erro e voltando a pedir as informações
"""

print("Login!")

credenciais = ["arthur", "123"]
while True:

    usuario = str(input("Digite o usuario:  "))
    senha = str(input("Digite a sua senha: "))

    if usuario == senha:
        print("Usuario e senha não podem ser iguais !")
        continue

    if usuario == "arthur" and senha == "123":
        print("Login validado!")
        break
    else:
        print("Tente novamente! ")
