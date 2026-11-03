from time import sleep
import os
def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

print('                         Olá, bem vindo ao HumaTec')
print(' ')
sleep(1.5)

while True:
    limpar_terminal()
    print('''                  Escolha um tópico para informações!!
============================================================================================
1. Conhecer profissões e suas aplicações de IA:
---------------------------------------------------------------------------------------------
Explore como a Inteligência Artificial está transformando diferentes áreas profissionais
e conheça exemplos de sua utilização no cotidiano
============================================================================================
2. Descobrir tarefas que podem receber auxílio da IA:
-------------------------------------------------------------------------------------------
Conheça exemplos de tarefas automatizáveis e entenda como essas ferramentas podem
contribuir para diferentes áreas:
============================================================================================
3. Participar de um desafio sobre habilidades humanas:
-------------------------------------------------------------------------------------------
Teste seus conhecimentos em um desafio interativo que apresenta situações do cotidiano
profissional envolvendo o uso da Inteligência Artificial. Em cada situação, escolha a
alternativa que representa a decisão mais responsável e que exige maior julgamento humano.
============================================================================================
4. Sair
============================================================================================
''')
    try:
        escolha = int(input(':'))
    except ValueError:
        print('Digite apenas números!!')
        continue

    match escolha:
        case 1:
            while True:
                limpar_terminal()
                print('='*50)
                print('1. Conhecer profissões e suas aplicações de IA:')
                print('''Escolha um exemplo:
[1]- Desenvolvedor de sistemas
[2]- Profissional da saúde
[3]- Professor
[4]- Designer
[S]- Sair''')
                print('='*50)
                escolha = str(input(':')).upper().strip()
                if escolha == '1':
                    print('-='*50)
                    print('Desenvolvedor de sistemas')
                    print(''' a IA pode sugerir trechos de código, identificar erros, auxiliar na documentação
e agilizar o desenvolvimento de softwares. Entretanto, o profissional continua responsável por compreender
os requisitos, testar as funcionalidades e garantir a segurança e o funcionamento do sistema.''')
                    print('-='*50)
                    sleep(5)
                    input('Pressione ENTER para voltar as opções')
                elif escolha == '2':
                    print('-='*50)
                    print('Profissional da saúde')
                    print('''Ferramentas de IA podem auxiliar na análise de exames, identificação de padrões e
organização de informações médicas. Ainda assim, o diagnóstico, a tomada de decisões e o
acompanhamento dos pacientes exigem avaliação e responsabilidade profissional.''')
                    print('-='*50)
                    sleep(5)
                    input('Pressione ENTER para voltar as opções')
                elif escolha == '3':
                    print('-='*50)
                    print('Professor')
                    print('''A IA pode ajudar na elaboração de atividades, criação de materiais didáticos, planejamento de
aulas e adaptação de conteúdos. O professor permanece essencial na orientação dos alunos, no
desenvolvimento do pensamento crítico e na compreensão das necessidades individuais da turma.''')
                    print('-='*50)
                    sleep(5)
                    input('Pressione ENTER para voltar as opções')
                elif escolha == '4':
                    print('-='*50)
                    print('Design')
                    print('''A IA pode gerar imagens, apresentar referências visuais, sugerir combinações e acelerar a criação
de projetos. Porém, o designer precisa avaliar os resultados, tomar decisões criativas e garantir que o
trabalho esteja de acordo com os objetivos do projeto.''')
                    print('-='*50)
                    sleep(5)
                    input('Pressione ENTER para voltar as opções')
                elif escolha == 'S':
                    print('Voltando para o menu...')
                    sleep(1)
                    break
                else:
                    print('Opção inválida!!')
                    continue
        case 2:
            print('2. Descobrir tarefas que podem receber auxílio da IA')
            print('''
            Alguas tarefas em que pode receber auxílio da IA são:
- Análise de dados: organização de grandes volumes de informações e identificação de padrões.
- Produção de conteúdo: auxílio na elaboração de textos, apresentações e materiais informativos.
- Programação: sugestão de códigos, identificação de erros e automatização de tarefas repetitivas.
- Atendimento: respostas automáticas a dúvidas frequentes e organização de solicitações.
- Criação visual: geração de imagens, ilustrações e referências para projetos gráficos.
''')
            print('''A IA pode assumir ou facilitar determinadas tarefas, mas isso não significa
necessariamente substituir toda a profissão.
''')
            sleep(5)
            input('Pressione qualquer ENTER para voltar ao menu')
        case 3:
            print('Teste seu conhecimento!!')
            erros = 0
            acertos = 0
            while True:
                while True:
                    sleep(0.6)
                    print('''
Pergunta 1 – Desenvolvedor de sistemas
Uma IA sugere um código para um sistema bancário. O que o desenvolvedor deve fazer?

A) Utilizar o código sem verificar seu funcionamento.
B) Revisar, testar e verificar a segurança do código antes de implementá-lo.
C) Pedir para a IA decidir se o código é seguro e encerrar a tarefa.''')
                    escolha = str(input(':')).upper()
                    sleep(1)   
                    if escolha == 'A':
                        print('''A IA pode cometer erros, essa opção poderia
comprometer todo o sistema!''')
                        erros += 1
                        break
                    elif escolha == 'B':
                        print('Opção correta!!')
                        acertos += 1
                        break
                    elif escolha == 'C':
                        print('A IA pode errar, essa opção não é viavel')
                        erros += 1
                        break
                    else:
                        print('Opção indisponivel!!')
                        continue
                sleep(1)
                while True:
                    print('''
Pergunta 2 – Profissional da saúde
Uma ferramenta de IA analisa os exames de um paciente e indica a possibilidade de uma doença. Qual deve ser a atitude do profissional da saúde?

A) Confirmar o diagnóstico exclusivamente com base na resposta da IA.
B) Ignorar completamente a análise feita pela ferramenta.
C) Avaliar os exames, considerar o histórico do paciente e utilizar a IA como ferramenta de apoio.
    ''')
                    escolha = str(input(':')).upper()
                    sleep(1)   
                    if escolha == 'A':
                        print('''A IA comete erros, essa opção é totalmente inviavel''')
                        erros += 1
                        break
                    elif escolha == 'B':
                        print('Poderia ocasionar na morte de uma pessoa!!')
                        erros+= 1
                        break
                    elif escolha == 'C':
                        print('Opção correta!!')
                        acertos += 1
                        break
                    else:
                        print('Opção indisponivel!!')
                        continue
                sleep(1)
                while True:
                    print('''
Pergunta 3 – Professor
Um professor utiliza uma IA para preparar uma aula, mas percebe que o conteúdo gerado não atende às dificuldades de aprendizagem de seus alunos. O que ele deve fazer?

A) Utilizar o material exatamente como foi gerado pela IA.
B) Adaptar o conteúdo de acordo com as necessidades dos estudantes e seus objetivos de aprendizagem.
C) Deixar que a IA escolha como os alunos devem aprender.
    ''')
                    escolha = str(input(':')).upper()
                    sleep(1)  
                    if escolha == 'A':
                        print('''O certo seria corrijir o material!!''')
                        erros += 1
                        break
                    elif escolha == 'B':
                        print('Opção correta!!')
                        acertos += 1
                        break
                    elif escolha == 'C':
                        print('Essa opção, pode impactar no futuro dos alunos!!')
                        erros += 1
                        break
                    else:
                        print('Opção indisponivel!!')
                        continue
                sleep(1)
                print('Parabens, você chegou ao final!!')
                sleep(0.5)
                print(f'Acertos: {acertos}')
                sleep(0.8)
                print(f'Erros: {erros}')
                sleep(2)
                print(' ')
                input('Pressione ENTER para voltar ao menu')
                break
        case 4:
            print('Tchauu, até a próxima!!')
            break
        case _:
            print('Opa!')
            sleep(0.6)
            print('Essa opção é inválida!!')
            sleep(1)
