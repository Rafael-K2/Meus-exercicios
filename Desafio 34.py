s = int(input('Qual seu salário ?'))
if s <= 1250:
    a = (15/100 * s)+s
    print('Seu salário é de R${}'.format(a))
else:
    a2 = (10/100 * s)+s
    print('Seu salário é de R${}'.format(a2))