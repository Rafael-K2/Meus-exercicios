'''c = str(input('Seu nome:'))
s = c.find('silva')
print(s)
Tem bugs
'''
nome = str(input('Seu nome completo')).strip()
print('Seu nome tem silva {}'.format('silva' in nome.lower()))