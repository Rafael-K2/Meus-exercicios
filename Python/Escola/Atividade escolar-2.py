print('Atividade 1')

l1 = int(input('Lado 1 do triangulo'))
l2 = int(input('Lado 2 do triangulo'))
l3 = int(input('Lado 3 do triangulo'))

if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    if l1 == l2 == l3:
            print('É um triangulo equilátero')
    elif l1 == l2 or l2 == l3 or l1 == l3:
        print('É um triangulo isósceles')
    else:
        print('É um triangulo escaleno')
else:
    print('Triangulo não pode ser formado')

print("Atividade 2")
dia = int(input("Qual o dia que você nasceu: "))
mes = int(input("Qual o mês que você nasceu: "))
ano = int(input("Qual o ano que você nasceu: "))

bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

if mes == 2:
    if bissexto and dia > 29:
        print("Fevereiro em ano bissexto tem no máximo 29 dias!")
    elif not bissexto and dia > 28:
        print("Fevereiro em ano normal tem no máximo 28 dias!")
    else:
        print("Data válida")

elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    if dia > 31:
        print(f"O dia não pode ser maior do que 31 no mes {mes}!")
    else:
        print("Data válida")

elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if dia > 30:
        print(f"O mes {mes} não pode ter dia maior que 30!")
    else:
        print("Data válida")

else:
    print("Mês inválido!")

print('atividade 3')

hora_entrada = int(input('Hora de entrada: '))
minuto_entrada = int(input('Minuto de entrada: '))
hora_saida = int(input('Hora de saída: '))
minuto_saida = int(input('Minuto de saída: '))

if hora_entrada < 0 or hora_entrada > 23 or minuto_entrada < 0 or minuto_entrada > 59:
    print('Horário de entrada inválido')

elif hora_saida < 0 or hora_saida > 23 or minuto_saida < 0 or minuto_saida > 59:
    print('Horário de saída inválido')

else:
    entrada = hora_entrada * 60 + minuto_entrada
    saida = hora_saida * 60 + minuto_saida

    if saida <= entrada:
        print('A saída deve ser posterior à entrada')

    else:
        tempo = saida - entrada

        if tempo <= 60:
            print('Valor: R$ 5,00')

        elif tempo <= 180:
            print('Valor: R$ 10,00')

        elif tempo <= 360:
            print('Valor: R$ 15,00')

        else:
            print('Valor: R$ 25,00')

print('atividade 4')

valor = int(input('Valor do saque: '))

if valor <= 0:
    print('Valor inválido')

elif valor % 10 != 0:
    print('O valor deve ser múltiplo de 10')

else:
    notas100 = valor // 100
    resto = valor % 100

    notas50 = resto // 50
    resto = resto % 50

    notas20 = resto // 20
    resto = resto % 20

    notas10 = resto // 10

    print('Notas de R$ 100:', notas100)
    print('Notas de R$ 50:', notas50)
    print('Notas de R$ 20:', notas20)
    print('Notas de R$ 10:', notas10)

print('atividade 5')

import random

numero_secreto = random.randint(1, 100)

tentativa = int(input('Digite sua tentativa (1 a 100): '))

if tentativa < 1 or tentativa > 100:
    print('Tentativa inválida')

else:
    if tentativa == numero_secreto:
        print('Acertou!')

    elif tentativa > numero_secreto:
        diferenca = tentativa - numero_secreto

        if diferenca <= 5:
            print('Muito próximo')

        elif diferenca <= 15:
            print('Próximo')

        else:
            print('Longe')

        print('O número secreto é menor')

    else:
        diferenca = numero_secreto - tentativa

        if diferenca <= 5:
            print('Muito próximo')

        elif diferenca <= 15:
            print('Próximo')

        else:
            print('Longe')

        print('O número secreto é maior')