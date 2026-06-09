print('Seu caminhão aguenta até 1000Kg')
total = 1000
qkgc = 0
while True:
    if total <= 1000:
        colocar = int(input('Quantos Kg vc quer colocar ?'))
        total -= colocar
        qkgc += 1
        print(f'Ainda falta {total}Kg para encher!')
        if total == 0:
            print(f'Limite atingido voce colocou peso {qkgc} vezes')
            break
        elif total < 0:
            print(f'Passou do limite em {-total}, Cuidado!')
            break