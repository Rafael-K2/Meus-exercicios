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
c = float(input('Quantos celcios vc quer transformar: '))
f = c * 9 / 5 + 32
print(f'Em Fahrenheit ficaria :{f:.2f}')
# 0 ficou com 32
# 25 ficou 77
# -10 ficou 14
#===========================================================#

print('Atividade 5')
caderno = int(input('Preço do carderno: '))
quantia_caderno = int(input('Quantos cardernos: '))
valor_recebido = int(input('Valor recebido: '))

valor_pagar = caderno * quantia_caderno
troco = valor_recebido - valor_pagar

print(f'O troco é de {troco:.2f}R$')
#===========================================================#

print('Atividade 6')
a = 4
b = a
a = 9
c = a + b
#Por que eu alterei o A apos alterar o B, teria q alterar B dnv pra ser igual a A
#===========================================================#

print('Atividade 7')
#Não funciona pq ele não especificou para o py q o input é inteira
idade = int(input('Idade: '))
print(idade+1)
#===========================================================#

print('Atividade 8')
'''Cep e quantidade de alunos, se encaixa bem no INT, para preços o float é o melhor,
e para verdadeiro ou falso é o boolean'''
cep = int(input('Qual seu CEP: '))
quantidade_alunos = int(input('Quantos alunos na sala: '))
preço_caderno = float(input('Preço do caderno: '))
verdadeiro_falso = bool(input('Verdadeiro ou falso: '))
#===========================================================#

print('Atividade 9')
nome = str(input('Qual seu nome: '))
idade = int(input('Qual sua idade: '))
cidade = str(input('Qual sua cidade: '))
curso = str(input('Qual curso vc quer: '))

n_idade = idade+1

print(f'''
Nome:{nome}
Idade:{idade}
Idade no proximo ano:{n_idade}
Cidade:{cidade}
Curso{curso}
''')
#===========================================================#

# Tópico 2 - Operadores e expressões

print('Questão 10')
'''
O 17 % 5 é quem mostra quantas vezes o 5 cabe no 17
'''
#===========================================================#

print('Questão 11')
#Os parenteses mudam a forma que a operação vai ser feita, oq tá dentro do parentese é feito primeiro
n1 = 5
n2 = 6
n3 = 8
media = (n1 + n2 + n3 ) / 3
#===========================================================#
print('Questão 12')
total_segundos = int(input("Digite o total de segundos: "))

horas = total_segundos // 3600
resto_horas = total_segundos % 3600
minutos = resto_horas // 60
segundos_restantes = resto_horas % 60

print(f"{total_segundos} segundos devem resultar em {horas} hora(s), {minutos} minuto(s) e {segundos_restantes} segundo(s).")
#===========================================================#
print('Questão 13')
n1 = 3
n2 = 6
n3 = 9
n1 = n1 * 2
n2 = n2 * 3
n3 = n3 * 5
resultado = (n1 + n2 + n3) / (2 + 3 + 5)
print(resultado)
#===========================================================#
print('Questão 14')
pecas = int(input("Digite a quantidade de peças: "))
capacidade = int(input("Digite a capacidade da caixa: "))

caixas_completas = pecas // capacidade

sobra = pecas % capacidade

if sobra > 0:
    caixas_totais = caixas_completas + 1
else:
    caixas_totais = caixas_completas

print(f"{caixas_completas} caixas completas")
print(f"{sobra} peças restantes")
print(f"{caixas_totais} caixas necessárias")
#===========================================================#
print('Questão 15')
idade = 17
autorizado = True
acompanhado = False

print(idade >= 18 or autorizado)   # True Vai verificar se pelomenos algumas das condições são verdadeiras
print(idade >= 18 and autorizado)  # False Verifica se as duas são verdadeiras
print(not acompanhado)             # True Inverte o valor boleano

#===========================================================#
print('Questão 16')
"""
Inverter o denominador com o numerador, faz com que
o desconto apareça em forma decimal, dps multiplica por 100 para virar porcentagem
"""

#===========================================================#
print('Questão 17')

#===========================================================#
print('Questão 18')

#===========================================================#
# Tópico 3 - Estruturas condicionais

print('Questão 19')

'''
O if Serve para criar uma condição, o elif é usando para
uma segunda condição, e o else e caso nenhuma das condições
for verdadeira
'''
#===========================================================#
print('Questão 20')
n = int(input('Numero qualquer: '))
if n % 2 == 0:
    print('Número par')
elif n % 2 == 1:
    print('Número impar')
else:
    print('Inválido')
#===========================================================#
print('Questão 21')
n1 = int(input('Valor1: '))
n2 = int(input('Valor2: '))
if n1 > n2:
    print(n1,'é maior')
elif n2 > n1:
    print(n2,'é maior')
else:
    print('São valores iguais')
#===========================================================#
print('Questão 22')
n1 = int(input('Nota 1: '))
n2 = int(input('Nota 2: '))

media = (n1 + n2) / 2

if media >= 7:
    print('aprovado')
elif media > 4 and media < 7:
    print('recuperação')
else:
    print('reprovado')

#===========================================================#
print('Questão 23')
#===========================================================#
print('Questão 24')
#===========================================================#
print('Questão 25')
#===========================================================#
print('Questão 26')
#===========================================================#
print('Questão 27')
#===========================================================#
print('Questão 28')
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
#===========================================================#
print('Questão 29')
#===========================================================#
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

# Tópico 7 - Listas e matrizes

# Tópico 8 - Tuplas, dicionários e conjuntos

# Tópico 9 - Funções, decomposição e recursão

print('Atividade 73')
def dobro(numero):
    numero = numero * 2
    return numero #O return vai guardar o valor da operação acima, na variavel "numero"
    
numero = int(input('Qual número vc quer ver o dobro: '))
n = dobro(numero) #Aqui é onde eu coleto o valor do return da função
print(n)#Aqui eu imprimo
#===========================================================#

print('Atividade 74')
def versão_a(a,b):
    print(a+b)
def versão_b(a,b):
    return a + b
    
a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
versão_a(a,b)
resultado = versão_b(a,b)
mult_a = versão_a(a,b) * 3
mult_b = resultado * 3
print(mult_a)
print(mult_b)

'''
Usar a versão A vai ocasionar na falta
de retorno de valor, ou seja, quando ela
recebe os valores, ela sempre retorna NONE.
Logo, quando vamos fazer a operação, o py entende
como NONE * 3, Por isso da erro
'''
#===========================================================#

print('Atividade 75')
def celsius_para_fahrenheit(c):
    f = c * 9/5 + 32
    return f
def fahrenheit_para_celsius(f):
    c = (f - 32) * 5 / 9
    return c
    
print('''
Quer transformar F para c, ou C para F ?

C para F digite: 1
F para C digite: 2
''')
escolha = int(input(': '))
if escolha == 1:
    c = int(input('Quantos C vc quer transformar: '))
    f = celsius_para_fahrenheit(c)
    print(f)
elif escolha == 2:
    f = int(input('Quantos f vc quer transformar: '))
    c = fahrenheit_para_celsius(f)
    print(c)
#===========================================================#

print('Atividade 76')
#===========================================================#

print('Atividade 77')
#===========================================================#

print('Atividade 78')
#===========================================================#

print('Atividade 79')
#===========================================================#

print('Atividade 80')
#===========================================================#

print('Atividade 81')
#===========================================================#