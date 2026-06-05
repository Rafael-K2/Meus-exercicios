print('Qual suas duas notas ?')
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
m = (n1 + n2) / 2

if m < 5:
    print('Você está reprovado')
elif 5 <= m <= 6.9:
    print('Está de recuperação')
elif m >= 7:
    print('Aprovado')