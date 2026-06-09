total = 0

while True:
    valor = int(input('Quanto vc quer colocar no cofre: '))
    total += valor

    if valor == 0:
        break
print(f'No seu cofre tem {total}R$')