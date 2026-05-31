'''a = int(input('O ano em q vc está tem 365 dias, ou 366? '))
if a == 366:
    print('é um ano bissexto')
else:
    print('é um ano normal')
    Funciona, mas tem jeitos melhores
    '''
ano = int(input('Que ano quer analisar'))
if ano % 4 == 0 and ano % 100 != 0 or ano% 400 == 0 :
    print('Ano BISSEXTO')
else:
    print('Não é BISSEXTO')