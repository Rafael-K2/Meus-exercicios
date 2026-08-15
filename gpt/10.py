lista = [
    {'nome':'Carlos','nota':10}
]

def cadastrar_aluno(nome,nota):
    cad = {}
    cad['nome'] = nome  
    cad['nota'] = nota  
    lista.append(cad)

nome = str(input('Nome:'))
nota = int(input('Nota:'))
resultado = cadastrar_aluno(nome,nota)

print('Aluno cadastrado com sucesso')