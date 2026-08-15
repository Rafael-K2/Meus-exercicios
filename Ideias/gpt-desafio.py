alunos = [
    {"nome": "João", "nota": 7.5},
    {"nome": "Maria", "nota": 9.0},
    {"nome": "Pedro", "nota": 5.5},
    {"nome": "Ana", "nota": 8.0},
    {"nome": "Lucas", "nota": 6.0}
]

aluno_com_maior_nota = 0
aluno_com_menor_nota = 1000000
melhor_aluno = None
for aluno in alunos:
    if aluno['nota'] > aluno_com_maior_nota:
        aluno_com_maior_nota = aluno['nota']
        melhor_aluno = aluno['nome']
print(f'''O aluno com maior nota foi:{melhor_aluno}
com:{aluno_com_maior_nota}''')

pior_aluno = None
for aluno in alunos:
    if aluno['nota'] < aluno_com_menor_nota:
        aluno_com_menor_nota = aluno['nota']
        pior_aluno = aluno["nome"]
print(f'''O aluno com meno nota foi:{pior_aluno}
com:{aluno_com_menor_nota}''')

aluninhos = len(alunos)
total_da_turma =0
for aluno in alunos:
    total_da_turma += aluno["nota"]
media = total_da_turma / aluninhos
print(f'''A média de toda a turma é de {media}''')

acima_da_media = 0
for aluno in alunos:
    if aluno["nota"] > media:
        acima_da_media += 1
print(f'Existem {acima_da_media} alunos acima da média')