v = int(input('Qual a velocidade do seu carro ? '))
m = 7
r = 7*(v-80)
if v > 80:
    print('Está no limite')
else:
    print('Sua multa será de R${}'.format(r))