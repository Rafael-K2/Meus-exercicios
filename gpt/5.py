print('Maquina de moedas')
m = int(input('Digite um valor: '))
v = m
ced = 5
totced = 0
while True:
    if v >= ced:
        v -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de moedas é de {totced} cedulas de {ced}R$')
        if ced == 5:
            ced = 2
        elif ced == 2:
            ced =1
        totced = 0
        if v == 0:   
            break
            