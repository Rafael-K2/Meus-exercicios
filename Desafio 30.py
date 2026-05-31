'''
a = int(input('Digite um número ente 1 é 10 '))
if a == 2 or 4 or 6 or 8 or 10 :
    print('Seu número é par')
else:
    print('Seu número é impar')
    Funciona, mas só entre 1 é 10
    '''
n = int(input('Mé diga um número: '))
r = n % 2
if r == 0:
    print('O número {} é par'.format(n))
else:
    print('O número {} é Impar'.format(n))