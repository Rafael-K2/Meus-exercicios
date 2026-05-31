import random
print('Adivinhe o número entre 0 e 5')
n = random.randint(0, 5)
r = int(input('Digite o número q vc acha q é: '))
if r == n:
    print('Você acertou!')
else:
    print('Que pena, você errou')