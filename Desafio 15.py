print('Esse programa calcula o alugueu de um carro')
d = float(input('Quantos dias alugados ? '))
k = float(input('Quantos KM rodados ? '))
dr = d * 60
kr = k * 0.15
cobrar = dr + kr
print('Seu aluguel é de R${:.2f}'.format(cobrar))