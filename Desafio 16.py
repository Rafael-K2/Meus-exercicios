print("Esse programa mostra um número decimal sem suas casas decimais")
import math
n = float(input('Número q deseja transformar em inteiro:'))
i = math.trunc(n)
print('O seu número sem casas decimais é:{}'.format(i))