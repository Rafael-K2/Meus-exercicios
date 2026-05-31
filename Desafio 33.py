#Esse eu não soube fazer
a = int(input('Digite um número'))
b = int(input('Digite um número'))
c = int(input('Digite um número'))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior=b
if c > a and c > b:
    maior=c
print('O menor é {}'.format(menor))
print('O mair é {}'.format(maior))