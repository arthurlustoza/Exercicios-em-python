# Exercicio 1, não consegui entender a logica preciso estudar mais este tema
while True:
    valor = input("Digite uma nota entre 0 e 10: ")

    try:
        numero = float(valor)  # Usar float permite notas como 7.5

        if 0 <= numero <= 10:
            print(f"Valor aceito: {numero}")
            break  # Este comando ENCERRA o loop while imediatamente
        else:
            print(f"Nota fora do intervalo (0-10): {valor}")

    except ValueError:
        print(f"Entrada inválida! '{valor}' não é um número.")

print("Programa finalizado com sucesso.")
