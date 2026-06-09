from random import randint
v = 0
while True:
    c = randint(1, 10)
    j = int(input('Adivinhe o número q eu pensei: '))
    if j == c:
        print('Vc venceu!')
        v += 1
    else:
        print('Vc Perdeu')
        break
print(f'vc ganhou {v} vezes')