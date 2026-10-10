from time import sleep
saldo = 100
sacar = 0
while True:
    escolha = int(input(
    '''Escolha oq vc quer fz
    [ 1 ] Sacar
    [ 2 ] Depositar
    [ 3 ] Mostrar saldo
    [ 4 ] Sair 
    '''))
    sacar = saldo - sacar
    if escolha == 1:
        if sacar <= saldo:
            print(f'Vocé tem de {saldo:.2f}R$')
            sacar = float(input('Quanto quer sacar ?: '))
            saldo = saldo - sacar
            print(f'Agora vc tem {saldo:.2f}R$ na sua conta')
            sleep(1)
        else:
            print('Você não pode mais sacar')
            sleep(1)
    elif escolha == 2:
        depositar = float(input('Quanto vc quer depositar: '))
        saldo = depositar + saldo
        print(f'Seu saldo é de {saldo:.2f}R$')
        sleep(1)
    elif escolha == 3:
        print(f'Seu saldo é de {saldo}R$')
        sleep(1)

    elif escolha == 4:
        print('Até a proxima!')
        break