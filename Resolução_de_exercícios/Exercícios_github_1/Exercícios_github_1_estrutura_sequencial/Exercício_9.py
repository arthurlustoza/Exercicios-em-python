'''
Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9)
Mostrar apenas valor inteiro da temperatura
'''
print("Conversor de temperatura!")

fah = float(input('Digite a temperatura em fahrenheit:'))

c = 5 * ((fah-32)/  9)

print(f"Temperatura em celcius e de: {c:.0f}")