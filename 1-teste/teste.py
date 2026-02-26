
#Testes 
a = 7 * 3 + \
5/2


b = ['a', 'b', 'c', 'd', 'e']


c = range(1,
12)


print (a, b, list(c))

#Estrutura de repetição 
for i in [234, 654, 378, 798]:

    if i % 3 == 0:

        print(i, '/ 3 =', i /3)


temp = float (input('Entre com a temperatura: '))

if temp > 0 and temp < 32:
        print ("Dá para sair de casa")
elif temp > 32:
        print("Muito quente")

s = 0
for x in range(1, 100):
            s = s + x
            print (s)