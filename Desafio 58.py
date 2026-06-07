from random import randint
n = randint(1, 10)
num = int(input('Adivinhe o número inteiro entre 1 é 10: '))
while n != num:
    num = int(input('Adivinhe o número inteiro entre 1 é 10: '))
print("Isso ai acertou")