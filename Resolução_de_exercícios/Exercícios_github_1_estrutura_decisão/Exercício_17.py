import sys
import math

print("Calculadora de raízes")

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

if a == 0:
    print("Equação não é de segundo grau")
    sys.exit()

delta = b**2 - 4 * a * c

if delta < 0:
    print(f"Delta negativo: {delta}, por isto não existem raízes reais")
elif delta == 0:
    x = -b / (2 * a)
    print(f"Delta: {delta}, raiz única: {x}")
else:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f"Delta: {delta}, raízes reais: {x1} e {x2}")

# feito por ia, não entendi a logica
