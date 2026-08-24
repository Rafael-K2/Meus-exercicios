"""Adivinhação (nível 2)
limitar tentativas (ex: 5 chances)
mostrar “restam X tentativas”
reiniciar o jogo no final"""

from random import randint
from time import sleep

tentativas = 5
while True:
    pc = randint(1,5)
    jogada = int(input('Entre 1 é 5, qual o número que eu pensei ?'))
    if jogada == pc:
        tentativas -= 1
        print(f'Você acertou, leu minha mente hahaha\nVocê acertou faltando {tentativas} tentativas, meus parabéns')
        break
    else:
        tentativas -=1
        print(f'Que pena você errou, ainda lhe restam {tentativas} tentativas!')
    if tentativas == 0:
        print('Suas tentativas acabaram, quer tentar denovo ?')
        jogar_novamente = str(input('[S/N]\n:')).upper()
        if jogar_novamente == 'S':
            print('Então vamos lá')
            print('Carregando...')
            sleep(1)
            continue
        elif jogar_novamente == 'N':
            print('Sem problemas, té vejo na proxima!')
            break
        else:
            print('Vou considerar um não')
            break