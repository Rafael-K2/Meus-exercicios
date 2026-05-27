print('Esse programa mostra o quanto de tinta vc vai usar pra pintar uma parede')
altura = int(input('Qual a altura da parede ?'))
largura = int (input('Qual a largura da parede ?'))
area = altura * largura
tinta = area / 2
print('A quantidade de tinta que vc vai usar é de {}M²'.format(tinta)) 