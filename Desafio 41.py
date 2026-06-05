print('Vou te dizer sua classificação de nadador\nde acordo com sua idade')
i = int(input('Qual sua idade ?'))
if i <= 9:
    print('Você é um nadador Mirim')
elif i <= 14:
    print('Você é um nadador Infantil')
elif i <= 19:
    print('Você é um nadador Junior')
elif i == 20:
    print('Você é um nadador Sênior')
elif i > 20:
    print('Você é um nadador master')