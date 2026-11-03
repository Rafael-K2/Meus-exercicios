'''
Nome:Carlos Rafael Silva Soares     Turma: 1° Desenvolvimento de sistemas
Professora:Pryscilla                Data: 09/10/2026
print('Exercicio 1')

musicas = ['eu pensei','canal','chorar na beira do mar','lugar de agonia','eternamente']
q_musicas = len(musicas)

print('As atuais músicas são:')
for i in musicas:
    print(i, end=', ')

print(f'Primeira música: {musicas[0]} ultima música: {musicas[-1]}')

print(f'Músicas na playlist: {q_musicas}')

musicas_ordenadas = sorted(musicas)

for i in musicas_ordenadas:
    print(i, end=', ')
'''
print('Exercicio 2')

convidados = ['C.Rafeel','Romario','Kelton','jesse','geovane']

for i in convidados:
    print(i, end=', ')