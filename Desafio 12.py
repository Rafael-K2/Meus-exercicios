print('Me fale o preço do seu produto, e eu vou mostrar\no valor dele com 5% de desconto')
p = int(input('Qual o preço do seu produto ?'))
d = 5/100 * p
pt = p-d
print('O valor do seu produto com 5% de desconto é{}'.format(pt))