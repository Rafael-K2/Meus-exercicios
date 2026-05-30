import math
print('Esse programa calcula a hipotenusa de um triangulo retangulo')
co = int(input('Qual o cateto oposto:'))
ca = int(input('Qual o cateto adjacente:'))
s= math.pow(co,2) + math.pow(ca,2)
h = math.sqrt(s)
print('A hipotenusa vale {}'.format(h))
#usando math.hypot, ele já faz o calculo da hipotenusa utilizando somente os dados dos catetos