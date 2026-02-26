'''
Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
Mostrar apenas valor inteiro da temperatura
F = (C × 9/5) + 32
'''

print("Convertor de temperatura!")

c = float(input('Digite a temperatura em Celcius: '))

f = (c * 9/5) + 32

print(f"Temperatura em fah: {f:.0f} f")