
def buscar (alunos,nome):
    for aluno in alunos:
        if nome == aluno['nome']:
            return aluno


    return None

def mudar_nota(alunos,nome,nova_nota):
    op = buscar(alunos, nome)
    if op == None:
        return None
    else:
        op['nota'] = nova_nota
        return op
    
def remover_aluno(alunos,nome):
    al = buscar(alunos,nome)
    if al == None:
        return None
    else:
        alunos.remove(al)
        return al
    

alunos = [
    {'nome':'Rafael', 'idade': 17, 'nota': 10},
    {'nome':'Isabelly', 'idade': 15, 'nota': 9},
    {'nome':'Bruno', 'idade': 18, 'nota': 5},
    {'nome':'Naiara', 'idade': 15, 'nota': 7}
]


melhor_aluno = 0
aluninho = None
for aluno in alunos:
    if aluno['nota'] > melhor_aluno:
        melhor_aluno = aluno['nota']
        aluninho = aluno['nome']
print(melhor_aluno,aluninho)


total_alunos = len(alunos)
total_notas = 0
for aluno in alunos:
    total_notas += aluno['nota']

media = total_notas / total_alunos
print(media)

aprovados = [

]
for aluno in alunos:
    if aluno['nota'] >= 7:
        aprovados.append(aluno)
        print(aluno['nome'])

print(aprovados)

melhores_alunos = [

]
for aluno in alunos:
    if aluno['nota'] >= 8:
        melhores_alunos.append(aluno)
        print(aluno['nome'])

alunos_aprovados = [

]
for aluno in alunos:
    if aluno['nota'] >= 7 and aluno['idade'] >= 16:
        alunos_aprovados.append(aluno)
        print(aluno['nome'])

for aluno in alunos:
    aluno['nota'] = aluno['nota'] + 1
    print(aluno['nota'])

for aluno in alunos:
    if aluno['nota'] < 7:
        aluno['nota'] += 2
    print(aluno)

op = buscar(alunos,'Naiara')
print(f'''{op['nome']}
{op['idade']}
{op['nota']}''')


nova_nota = int(input('Qual a nova nota do aluno:'))
nome = str(input('Nome do aluno:'))
resultado = mudar_nota(alunos,nome,nova_nota)
if resultado == None:
    print('Aluno inesistente')
else:
    print(resultado['nome'],resultado['nota'])

resultado = remover_aluno(alunos, 'Bruno')
print('Aluno removido:',resultado)

print(alunos)