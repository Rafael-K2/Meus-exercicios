soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {} Valor: '.format(c)))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print('vc informou {} pares e a soma deles foi {}'.format(cont, soma))