from random import randint
v = 0
while True:
    jogador = int(input('Escolha um número: '))
    computador = randint(1, 10)
    soma = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar [P/I]: ')).strip().upper()[0]
        print(f'Vc jogou {jogador} e o computador jogou {computador}. Total de {soma}')
        print('Deu par' if soma % 2 == 0 else 'Deu impar')
    if tipo == 'P':
        if soma % 2 == 0:
            print('Você venceu')
            v+=1
        else:
            print('Você perdeu')
            break
    elif tipo == 'I':
        if soma % 2 == 1:
            print('Você venceu')
            v+=1
        else:
            print('Você perdeu')
            break
    print('Vamos jogar novamente...')
print(f'Fim de jogo! Você venceu {v} vezes.')
