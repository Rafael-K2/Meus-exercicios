from random import randint
from time import sleep
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0,2)
print('''Sua opçõs:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada ?'))
print('Pedra')
sleep(1)
print('Papel')
sleep(1)
print('Tesoura')
print('-=' *11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' *11)
if computador == 0:
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador ganhou')
    elif jogador == 2:
        print('Jogador perdeu')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1:
        if jogador == 0:
            print('Jogador perdeu')
        elif jogador == 1:
            print('Empate')
        elif jogador == 2:
            print('Jogador ganhou')
        else:
            print('JOGADA INVÁLIDA')
elif computador == 2:
        if jogador == 0:
            print('Jogador perdeu')
        elif jogador == 1:
            print('Jogador ganhou')
        elif jogador == 2:
            print('Empate')
        else:
            print('JOGADA INVÁLIDA')
