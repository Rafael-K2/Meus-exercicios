nomes = []
while True:
    nome = (input('Digite algum nome:\n'))
    if nome == 'fim':
        break
    else:
        nomes.append(nome)
print('Nomes cadastrados:')
for n in nomes:
    print(f'{n}')

print('Quantidade de cadastros:',len(nomes))