import math
import random
from time import sleep
print('-='*20)
print('Esté é um app de teste para saber oq eu\naprendi em python no mundo 1 do\n       \033[4;32mGustavo Guanabara\033[m')
print('-='*20)
sleep(0.6)

print('\033[;34mAbrindo o app...\033[m')
sleep(1.5)

n = float(input('Escolha um número é veja se ele é par ou impar: '))
print('\033[;32mProcessando...\033[m')
sleep(2)

p = n % 2
if p == 0:
    print('O número que vc me deu é par')
    
else:
    print('O número é impar')
sleep(0.5)

print('Carregando proxima etapa...')
sleep(1)
print('\033[;35mEsse app lé a medida de tres retas, e diz se dá ou nn para fzr um triangulo\033[m')
sleep(2)

r1 = float(input('Reta 1: '))
r2 = float(input('Reta 2: '))
r3 = float(input('Reta 3: '))
print('Calculando...')
sleep(1)

if r1 < r2 + r3 and r2 < r1 + r2 and r3 < r1 + r2:
    print('\033[;32mvão formar um triangulo\033[m')
else:
    print('\033[;31mnão vão formar um triangulo\033[m')
sleep(0.8)

print('\033[;35mEsté é um calculador de multas, se passar de 80KM a multa será aplicada\nR$3 a cada KM a mais\033[m')
v = float(input('Quantos KM foi passado no radar: '))
print('\033[;31mProcessando multa...\033[m')
sleep(2)

multa = (v - 80) *3
if v >=80:
    print('A multa será de: \033[;31mR${}\033[m'.format(multa))
else:
    print('\033[;32mLivre de multa!\033[m')

print('Esta parte do app, vai analizar seu nome e dizer qual seu primeiro nome')
sleep(0.5)

nome = str(input('Qual seu nome ?')).strip()
print('Processando...')
sleep(0.5)

nd = nome.split()
print('Seu primeiro nome é:"{}" é seu ultimo nome é:"{}"'.format(nd[0],nd[len(nd)-1]))
print('Seu nome tem silva? {}'.format('silva' in nome.lower()))
sleep(1)
print('Esta parte do app é um mini jogo, se vc acertar o número\nque o computador pensou vc ganha')
sleep(1.5)
print('Adivinhe o número entre 0 é 5')
numero = random.randint(0, 5)
resposta = int(input('Qual número vc acha q é: '))
if resposta == numero:
    print('Parabens vc acertou!')
else:
    print('Vc errou que pena, boa sorte na proxima vez')