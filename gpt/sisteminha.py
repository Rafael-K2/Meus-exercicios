lista = [
    {
        "nome": "Rafael",
        "idade": 17,
        "nota": 9.5
    },
    {
        "nome": "João",
        "idade": 18,
        "nota": 8.0
    }
]

while True:
    cadastro = {}
    
    print('''Qual opção você quer ?
    [1] Cadastrar aluno
    [2] Listar alunos
    [3] Procurar aluno
    [4] Editar nota
    [5] Deletar cadastro do aluno''')
    
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