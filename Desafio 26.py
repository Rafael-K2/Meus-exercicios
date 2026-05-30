frase = str(input('Uma frase:')).upper().strip()
print('Tem {} letras A'.format(frase.count('A')))
print('A primeira: {}'.format(frase.find('A')+1))
print('A ultima: {}'.format(frase.rfind('A')+1))

#Resolvido com ajuda