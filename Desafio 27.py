nome = str(input('Qual seu nome:')).strip()
nd = nome.split()
print('Seu primeiro nome é:"{}" é seu ultimo nome é:"{}"'.format(nd[0],nd[len(nd)-1]))
#Usando o "len" da para saber o ultimo nome