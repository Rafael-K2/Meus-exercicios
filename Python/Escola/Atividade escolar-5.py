"""
Nome: Carlos Rafael Silva Soares
Série: 1°DS  Data 16/10/2026

""" 
# Topico 1 - Fundamentos, variáveis e entrada/saída
print('Questão 1')

valor_1 = 18 #INT
valor_2 = 7.5 #FLOAT
valor_3 = 'Python' #STRING
valor_4 = True #BOOLEAN

print(type(valor_1))
print(type(valor_2))
print(type(valor_3))
print(type(valor_4))

# ====================================================== #

print('Questão 2')

n1 = input('Digite um número: ')
n2 = input('Digite um número: ')

soma = n1 + n2

print(soma)

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))

soma = n1 + n2

print(soma)

'''
Usando o int, especificamos que o valor que colocamos alí é um número inteiro,
sem isso fica texto, por isso o resultado é diferente
'''

#===========================================================#

print('Atividade 3')
nome = str(input('Qual seu nome: '))
curso = str(input('Qual seu curso: '))
semestre = int(input('Em qual semestre você está: '))

print(f'''Nome: {nome}
Curso: {curso}
Semestre: {semestre}
Próximo semestre: {semestre + 1}''')
#===========================================================#

print('Atividade 4')

#===========================================================#

print('Atividade 5')

#===========================================================#

print('Atividade 6')

#===========================================================#

print('Atividade 7')

#===========================================================#

print('Atividade 8')

#===========================================================#

print('Atividade 9')

#===========================================================#

# Tópico 2 - Operadores e expressões

print('Questão 10')
'''
O 17 % 5 é quem mostra quantas vezes o 5 cabe no 17
'''
# Tópico 3 - Estruturas condicionais

print('Questão 19')

'''
O if Serve para criar uma condição, o elif é usando para
uma segunda condição, e o else e caso nenhuma das condições
for verdadeira
'''

n = 0

if n > 0:
    print('Positivo')
elif n < 0:
    print('Negativo')
else:
    print('É zero')

# Tópico 4 - Repetição com while e validação
n = 0
print('Questão 28')
while n < 0:
    print(n)
    n+= 1
    if n == 10:
        break

"""
Enquanto o n for menor que 0, o laço continua ele soma += 1
quando chegar n = a 10, o laço quebra e para

"""

# Tópico 5 - Repetição com for e laços aninhados
print('Questão 37')
"""
range(5) vai de 0 a 5
range(2,8) vai de 2 a 8
range(10,0,-2) vai de 10 a 0, de 2 em 2

"""
for n in range(5):
    print(n)
for n in range(2,8):
    print(n)
for n in range(10,0,-2):
    print(n)

# Tópico 6 - Strings e processamento de texto
print('Questão 46')
texto = "Programar"

print("Primeiro caractere:", texto[0])
print("Último caractere:", texto[-1])
print("Quatro primeiros caracteres:", texto[:4])
print("Tamanho do texto:", len(texto))