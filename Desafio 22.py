nome = (input('Qual seu nome completo:'))
print(nome.upper())
print(nome.lower())
print(len(nome.replace(' ','')))
d =nome.split()
print(len(d[0]))

'''COREÇÕES
O código funciona, mas poderia ser mais bonito.
Os comandos funcionam dentra da tag ".function()."
O ".strip" fica melhor no print em que a pessoa vai
escrever seu nome.
Para ler o nome todo sem contar os espaços pode se usar
print('asdasdas'.format(len(nome) - nome.count(' '))). '''