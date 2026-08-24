from time import sleep

lista = [
    {
        "nome": "Rafael",
        "idade": 17,
        "nota": 10
    },
    {
        "nome": "Belly",
        "idade": 18,
        "nota": 8.0
    },
    {
        "nome": "Bru",
        "idade": 15,
        "nota": 5
    },
    {
        "nome": "David",
        "idade": 16,
        "nota": 2
    },
    {
        "nome": "Nai",
        "idade": 16,
        "nota": 9.5
    }
]

while True:
    cadastro = {}
    
    print('''Qual opção você quer ?
    [1] Cadastrar aluno
    [2] Listar alunos
    [3] Procurar aluno
    [4] Editar nota
    [5] Deletar cadastro do aluno
    [6] Média dos alunos
    [7] Maior nota
    [8] Boletin da turma''')
    
    escolha = int(input('Sua escolha:'))

    if escolha == 1:
        cadastro['nome'] = str(input('Nome do aluno: '))
        cadastro['idade'] = int(input('Idade do aluno: '))
        cadastro['nota'] = float(input('Nota do aluno: '))
        lista.append(cadastro)
        print('Cadastro feito!')
    elif escolha == 2:
        for aluno in lista:
            print(f'''Nome:{aluno['nome']}
Idade:{aluno['idade']}
Nota{aluno['nota']}\n''')
    elif escolha == 3:
        aluno_selecionado = str(input('Qual aluno procura:'))
        encontrou = False
        for aluno in lista:
            if aluno['nome'] == aluno_selecionado:
                encontrou = True
                print('=-'*6)
                print(f"""Nome:{aluno['nome']}
Idade:{aluno['idade']}
Nota:{aluno['nota']}""")
                print('=-'*6)
                break
        if encontrou == False:
            print('Aluno não cadastrado')
                
    if escolha == 4:
        aluno_selecionado = str(input('Qual aluno você quer editar a nota:'))
        encontrou = False
        for aluno in lista:
            if aluno['nome'] == aluno_selecionado:
                encontrou = True
                nova_nota = float(input('Qual nota você que dar para esse aluno:'))
                aluno['nota'] = nova_nota
                print('Nota atualizada')
                break
        if encontrou == False:
            print('Aluno não cadastrado')

    if escolha == 5:
        aluno_selecionado = str(input('Qual aluno deseja deletar:'))
        encontrou = False
        for aluno in lista:
            if aluno['nome'] == aluno_selecionado:
                encontrou = True
                lista.remove(aluno)
                print('Aluno removido com sucesso!')
        if encontrou == False:
            print('Aluno não cadastrado')
    if escolha == 6:
        alunos = len(lista)
        nota = 0
        for aluno in lista:
            nota += aluno['nota']
        media = nota/alunos
        print(f'A média é de: {media}')
    if escolha == 7:
        maior_nota = 0
        melhor_aluno = None
        for aluno in lista:
            if aluno['nota'] > maior_nota:
                maior_nota = aluno['nota']
                melhor_aluno = aluno
        print(maior_nota, melhor_aluno['nome'])
    if escolha == 8:
        print('=-'*20)
        print(' '*10,'BOLETIN')
        print('=-'*20)
        for aluno in lista:
            if aluno['nota'] >= 7:
                print('=-'*20)
                print(f'''Nome: {aluno["nome"]}
Idade: {aluno['idade']}
Nota: {aluno['nota']}
Classificação: Aprovado''')
                print('=-'*20)
            elif aluno['nota'] >= 5 < 7:
                print(f'''Nome: {aluno["nome"]}
Idade: {aluno['idade']}
Nota: {aluno['nota']}
Classificação: Recuperação''')
                print('=-'*20)
            else:
                print(f'''Nome: {aluno["nome"]}
Idade: {aluno['idade']}
Nota: {aluno['nota']}
Classificação: Reprovado''')
                print('=-'*20)
                sleep(5)