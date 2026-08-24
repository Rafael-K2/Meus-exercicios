cadastrados = []
while True:
    nome = input('Qual nome você quer cadastrar ?')
    if nome == 'fim':
        break
    else:
        cadastrados.append(nome)
for n in cadastrados:
    print(n)

selecionar_nome = input('Qual nome você deseja procurar:')
if selecionar_nome in cadastrados:
    print('Nome cadastrado!')
else:
    print(f'Não está cadastrado')
    sim_ou_não = input(f'Deseja fazer o cadastro de {selecionar_nome}? [S/N]').upper()
    if sim_ou_não == 'S':
        cadastrados.append(selecionar_nome)
        print('Cadastro feito!!')
    else:
        print('Sem problemas!')
