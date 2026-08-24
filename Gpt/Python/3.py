import random
v = 0
while True:
    l = ['Pedra','Papel','Tesoura']
    c = random.choice(l)
    j = str(input('Pedra, Papel ou Tesoura ?')).strip().capitalize()
    print(f'O Computador escolheu {c}')
    if j == 'Pedra':
        if c == 'Pedra':
            print('EMPATE!')
        elif c == 'Papel':
            print('VC PERDEU')
            break
        elif c == 'Tesoura':
            print('VC GANHOU')
            v += 1
    elif j == 'Papel':
        if c == 'Pedra':
            print('VC GANHOU')
            v += 1
        elif c == 'Papel':
            print('EMPATE!')
        elif c == 'Tesoura':
            print('VC PERDEU')
            break
    elif j == 'Tesoura':
        if c == 'Pedra':
            print('VC PERDEU')
            break
        elif c == 'Papel':
            print('VC GANHOU')
            v += 1
        elif c == 'Tesoura':
            print('EMPATE!')
print(f'Você venceu {v} vezes')