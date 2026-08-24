import os

alunos = [
    {'nome': 'Rafael', 'idade': 17},
    {'nome': 'Isabelly', 'idade': 15}
]
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
def menu():
    print('''
╔════════════════════════╗
║      INFOSTUDENT       ║
╠════════════════════════╣
║ [1] Listar alunos      ║
║ [2] Cadastrar aluno    ║
║ [3] Buscar aluno       ║
║ [0] Sair               ║
╚════════════════════════╝
''')
    
def cadastrar(alunos):
    cad = {}
    cad['nome'] = str(input('Qual o nome do aluno:'))
    cad['idade'] = int(input('Qual a idade dele:'))

    alunos.append(cad)


def procurar_aluno(alunos):
    aluno_selecionado = str(input('Qual aluno vc está procurando:'))
    for aluno in alunos:
        if aluno['nome'] == aluno_selecionado:
            return aluno

    return None


while True:
    limpar_tela()
    menu()

    try:
        escolha = int(input(':'))
    except:
        print('Opção indisponivel, tente novamente!!')
        input('aperte ENTER para continuar!')
        continue

    if escolha == 1:
        limpar_tela()

        for aluno in alunos:
            print(f'''Nome: {aluno['nome']}
Idade: {aluno['idade']}''')
            print('-='*10)
        print(f'existem {len(alunos)} alunos cadastrados')
        input('aperte ENTER para continuar!')

    elif escolha == 2:
        limpar_tela()

        cadastrar(alunos)

        print('Aluno cadastrado com sucesso !')
        input('aperte ENTER para continuar!')

    elif escolha == 3:
        limpar_tela()

        op = procurar_aluno(alunos)
        if op:
            print(op['nome'])
            print(op['idade'])
        else:
            print('Aluno não encontrado!')
        input('aperte ENTER para continuar!')

    elif escolha == 0:
        print('Te vejo na proxima!')
        break