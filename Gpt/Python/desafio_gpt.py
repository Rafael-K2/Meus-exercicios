alunos = [
    {
    'nome': 'Rafael',
    'nota': 8.5
     },
    {
    'nome': 'Belly',
    'nota': 10
    }
]

while True:
    cadastro = {}

    print('''Opções
    [1] Cadastrar alunos
    [2] Lista dos alunos
    [3] Maior nota
    [4] Média da turma
    [5] Procurar aluno
    [6] Sair
    ''')
    escolha = int(input('Sua escolha:'))
    if escolha == 1:
        cadastro['nome'] = str(input('Qual o nome do aluno:')).capitalize()
        cadastro['nota'] = float(input('Qual a nota do aluno:'))
        alunos.append(cadastro)

        print(alunos)
    elif escolha == 2:
        for aluno in alunos:
            print(f'''Nome:{aluno['nome']}
Nota:{aluno['nota']}
-=-=-=-=-=-=-=-=-=-=-=-=''')
    elif escolha == 3:
        maior_nota = 0
        aluno_maior_nota = None
        for aluno in alunos:
            if maior_nota < aluno['nota']:
                maior_nota = aluno['nota']
                aluno_maior_nota = aluno['nome']
        print(f'''A maior nota é de {maior_nota} do aluno {aluno_maior_nota}''')
    elif escolha == 4:
        total_da_turma = 0
        total_de_alunos = len(alunos)

        for aluno in alunos:
            total_da_turma += aluno['nota']

        media = total_da_turma / total_de_alunos

        print(f'A média da turma é de {media}!')
    elif escolha == 5:
        aluno_escolhido = str(input('Qual aluno você está procurando:')).capitalize()
        for aluno in alunos:
            encontrou = False
            if aluno['nome'] == aluno_escolhido:
                encontrou = True
                print(f"""O aluno é: {aluno['nome']}
Com a nota de: {aluno['nota']}""")
                break
            else:
                print('''Esse aluno não existe, deseja cadastra-lo ?
[S/N]''')
                esc = str(input(':')).upper()
                if esc == 'S':
                    cadastro['nome'] = str(input('Qual o nome do aluno:')).capitalize()
                    cadastro['nota'] = float(input('Qual a nota do aluno:'))
                    alunos.append(cadastro)
                else:
                    print('Sem problemas')
    elif escolha == 6:
        print('Nos vemos na proxima!')
        break