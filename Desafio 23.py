'''
n = str(input('digite um número entre 0 e 9999: '))
d = n.split()
Não consegui resolver
'''
num = int(input('número'))
n = str(num)
print('unidade {}'.format(n[3]))
print('dezena {}'.format(n[2]))
print('centena {}'.format(n[1]))
print('milhar {}'.format(n[0]))
#Desse jeito, tem que ter o valor inteiro caso contrario dá erro.