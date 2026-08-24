lista = []

while True:
    cadastros = {}
    cadastros['nome'] = input('Qual seu nome: ')
    if cadastros['nome'] == 'fim':
        break
    else:
        cadastros['idade'] = int(input('Qual sua idade: '))
        cadastros['nota'] = float(input('Qual sua nota: '))
        lista.append(cadastros)
        

for item in lista:
    print(f'''nome: {item["nome"]}
idade: {item["idade"]}
nota: {item["nota"]}''')