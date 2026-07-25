inventario = ["poção", "moeda", "espada", "escudo", "mapa"]

for item in inventario:
    item_selecionado = input('Qual item vc procura: ')
    print(f'Procurando {item_selecionado}...')
    if item == item_selecionado:
        print('Item encontrado')
    else:
        print('Não encontrado')