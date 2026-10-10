import random

def criar_jogador(nome):
    jogador = {
        'nome': nome,
        'vida': 100,
        'ataque': 10,
        'ouro': 500
    }
    return jogador

def receber_dano(jogador,dano):
    jogador['vida'] = jogador['vida'] - dano
    return jogador

def criar_inimigo():
    inimigo = {
        'nome': 'goblin',
        'vida': random.randint(20,40),
        'ataque' : random.randint(3,8)
    }
    return inimigo

jogador = {

}

nome = str(input('Nome do seu perssonagem: '))
jogador = criar_jogador(nome)


dano = int(input('Dano de teste:'))
jogador = receber_dano(jogador,dano)

print(jogador)

inimigo = criar_inimigo()