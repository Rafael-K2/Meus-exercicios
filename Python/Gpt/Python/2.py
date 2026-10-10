from random import randint
v = 0
while True:
    c = randint(1, 10)
    j = int(input('Escolha um número: '))
    s = c + j
    tipo = ' '
    tipo = str(input('Par ou Impar ? [P/I]')).upper().strip()[0]
    print(f'Você jogou {j} e o computador {c}.')
    print(f'A soma deu {s}.')
    if tipo == 'P':
        if s % 2 == 0:
            print('Vc ganhou')
            v += 1
        else:
            print('Vc perdeu')    
            break
    elif tipo == 'I':
        if s % 2 == 1:
            print('Vc ganhou')
            v += 1
        else:
            print('Vc perdeu')
            break
print(f'Vc ganhou {v} vezes, parabens')