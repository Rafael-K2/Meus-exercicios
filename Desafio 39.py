i =int(input('Qual sua idade ?'))
f = i - 18
if i <= 17:
    print('Ainda não vai se alistar')
elif i == 18:
    print('Está na hr de se alistar')
elif i >= 19:
    print('já passou {} anos e vc n se alistou'.format(f))