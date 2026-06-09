num = ('zero','um','dois','tres','quatro','cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze' ,'quinze', 'dezesseis', 'dezesete', 'dezoito' ,'dezenove' ,'vinte')
for n in num:
    n = int(input('Escolha entre 0 é 20\n:'))
    if n > 20:
        print('Tente novamente')
    else:
        print((num[n]))