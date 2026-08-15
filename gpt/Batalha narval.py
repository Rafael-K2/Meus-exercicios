from random import randint
tab = [
    ['~','~','~','~','~'],
    ['~','~','~','~','~'],
    ['~','~','~','~','~'],
    ['~','~','~','~','~'],
    ['~','~','~','~','~']
]

tabuleiro = [
    ['~','~','~','~','~'],
    ['~','~','~','~','~'],
    ['~','~','~','~','~'],
    ['~','~','~','~','~'],
    ['~','~','~','~','~']
]

tabuleiro[randint(0,4)][randint(0,4)] = 'o'
tabuleiro[randint(0,4)][randint(0,4)] = 'o'
tabuleiro[randint(0,4)][randint(0,4)] = 'o'
tentativa = 1
for linha in tabuleiro:
    print(linha)
for linha in tab:
    print(linha)
while True:
    print('Qual coluna deseja atacar ?')
    coluna = int(input('coluna:'))
    linha = int(input('Linha:'))

    if tabuleiro[linha][coluna] == 'o':
        tab[linha][coluna] = 'N'
        print('Navio destruido!')
        print(f'Você precisou de {tentativa} tentativas pra acertar este navio')
    else:
        tab[linha][coluna] = 'X'
        print('Você acertou a água')
        tentativa += 1
    for linha in tab:
        print(linha)