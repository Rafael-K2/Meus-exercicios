print('Atividade 1')

letra = str(input('Digite sua letra: '))
vogal = "aeiou"

if letra in vogal:
    print("é uma vogal")
else:
    print('é consoante')
    
print('Atividade 2')

n1 = int(input('Qual a primeira nota do aluno: '))
n2 = int(input('Qual a segunda nota do aluno: '))
media = (n1+n2) /2

if media == 10:
    print('Parabens, nota máxima!')
elif media >= 7 and media <= 9:
    print('Aprovado!')
else:
    print('Reprovado')
    
print('Atividade 3')

n1 = int(input('Digite um número'))
n2 = int(input('Digite outro número'))
n3 = int(input('Digite outro número'))

if n1 > n2 and n1 > n3:
    print(f'O {n1} é o maior número')
elif n2 > n1 and n2 > n3:
    print(f'O {n2} é o maior número')
elif n3 > n2 and n3 > n1:
    print(f'O {n3} é o maior número')
    
print('Atividade 4')

n1 = int(input('Digite um número'))
n2 = int(input('Digite outro número'))
n3 = int(input('Digite outro número'))

if n1 > n2 and n1 > n3:
    print(f'O {n1} é o maior número')
elif n2 > n1 and n2 > n3:
    print(f'O {n2} é o maior número')
elif n3 > n2 and n3 > n1:
    print(f'O {n3} é o maior número')
    
if n1 < n2 and n1 < n3:
    print(f'O {n1} é o menor número')
elif n2 < n1 and n2 < n3:
    print(f'O {n2} é o menor número')
elif n3 < n2 and n3 < n1:
    print(f'O {n3} é o menor número')
    
print('Atividade 5')

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))

aux = a
a = b
b = aux

print('A =', a)
print('B =', b)


print('Atividade 6')

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

if a >= b and a >= c:
    if b >= c:
        print(a, b, c)
    else:
        print(a, c, b)

elif b >= a and b >= c:
    if a >= c:
        print(b, a, c)
    else:
        print(b, c, a)

else:
    if a >= b:
        print(c, a, b)
    else:
        print(c, b, a)


print('Atividade 7')

turno = input('Digite M, V ou N: ')

if turno == 'M':
    print('Bom Dia!')
elif turno == 'V':
    print('Boa Tarde!')
elif turno == 'N':
    print('Boa Noite!')
else:
    print('Valor Inválido!')


print('Atividade 8')

salario = float(input('Digite o salário: R$ '))

if salario <= 280:
    percentual = 20
elif salario <= 700:
    percentual = 15
elif salario <= 1500:
    percentual = 10
else:
    percentual = 5

aumento = salario * percentual / 100
novo_salario = salario + aumento

print('Salário antes do reajuste:', salario)
print('Percentual de aumento:', percentual, '%')
print('Valor do aumento:', aumento)
print('Novo salário:', novo_salario)