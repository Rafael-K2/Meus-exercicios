'''Nome: Carlos Rafael Silva Soares 1°DS'''

print('Exercicio 1')
from random import randint

print('Adivinhe o número')
print('Você tem 5 tentativas')

numero = randint(1,20)

tentativa = 5

ja_escolhidos = []
    
while True:
    escolha = int(input('Qual número vc escolhe entre 1 e 20: '))
    
    if escolha in ja_escolhidos:
        print('Você já escolheu esse número')
    else:
        ja_escolhidos.append(escolha)
    
    if escolha < 1 or escolha > 20:
        print('Escolha o valor entre 1 e 20!')
    else:
        if escolha == numero:
            print(f'Você acertou, o número era {numero}! Você tentou {tentativa} vezes')
            break
        else:
            tentativa -= 1
            print(f'Você errou, lhe restam {tentativa} tentativas')
            
            if numero > escolha:
                print('O número é maior')
            else:
                print('O número é menor')
                
        if tentativa == 0:
            print(f'Suas tentativas esgotaram ! o número era {numero}')
            break
        
'''
• Qual estrutura controlará as cinco tentativas?
Contrala com uma variavel pre definida com 5, a cada tentativa é retirado 1 
e quando chega 0 o break faz o loop encerrar

• Como o programa poderá encerrar antes da quinta tentativa?
verificando antes

• Como os palpites anteriores poderão ser armazenados?
eles são armazenados em uma lista

• Qual condição controlará uma nova partida?
Não existe uma forma de reiniciar em si, você tem q executar denovo
mas se as tentativas chegar a 0 o jogo acaba
'''

print('Exercicio 2')

senha = '1234'
saldo = 1000
tentativas_senhas = 3
alteracoes = 0

print('Bem vindo ao caixa eletrônico')
print('Qual sua senha')

while True:
    senha_digitada = str(input(':'))

    if len(senha_digitada) != len(senha):
        print(f'Você usou {len(senha_digitada)} digitos, a senha é de 4 digitos!')
    else:
        if senha_digitada == senha:
            print('Você entrou')
            while True:
                print('''Opções disponiveis:
    [1]- Consultar saldo
    [2]- Realizar saque
    [3]- Realizar depósito
    [0]- Sair''')
                opcao = int(input(':'))
                if opcao == 1:
                    print(f'O seu saldo é de {saldo}R$')
                elif opcao == 2:
                    if saldo < 0:
                        print('Você não tem dinheiro para sacar!')
                    else:
                        print('Quanto você deseja sacar ?')
                        saque = int(input(':'))
                        if saque > saldo:
                            print(f'Você tem {saldo}R$ não pode sacar {saque}R$')
                        else:
                            saldo -= saque
                            alteracoes += 1
                            print('Saque feito!')
                elif opcao == 3:
                    print('Quanto você que depósitar')
                    deposito = int(input(': '))
                    if deposito <= 0:
                        print('Você não pode depositar 0 ou menos!')
                    else:
                        saldo += deposito
                        alteracoes += 1
                        print('Deposito feito!')
                elif opcao == 0:
                    print(f'Você fez {alteracoes} alterações!')
                    print('Obrigado por escolher nosso caixa')
                else:
                    print('Essa opção não existe')
        else:
            tentativas_senhas -= 1
            print(f'Senha incorreta, lhe restam {tentativas_senhas} tentativas!')
        if tentativas_senhas == 0:
            print('Suas tentativas acabaram')
            break

'''
• Qual laço controlará as tentativas de senha?
• Qual laço controlará o menu?
• Em que situações o programa deve usar um contador?
• Como impedir que o saldo se torne negativo?
'''

print('Exercício 3')
print('Votação para projeto')

print('''Escolha qual projeto você quer:
[1]- Desenvolvimento de jogos
[2]- Aplicativo educacional
[3]- Sistema para comercio local
[0]- Encerrar votação
''')

escolha_1 = 0
escolha_2 = 0
escolha_3 = 0
invalidos = 0
validos = 0

while True:
    escolha = int(input('Sua escolha: '))

    if escolha == 1:
        escolha_1 += 1
        validos += 1
        print('Você escolheu desenvolvimento de jogos')

    elif escolha == 2:
        escolha_2 += 1
        validos += 1
        print('Você escolheu aplicativo educacional')

    elif escolha == 3:
        escolha_3 += 1
        validos += 1
        print('Você escolheu sistema para comercio local')

    elif escolha == 0:
        print('Votação encerrada!')
        break

    else:
        invalidos += 1
        print('Votação inválida!')


print(f'''
Desenvolvimento de jogos: {escolha_1} votos
Aplicativo educacional: {escolha_2} votos
Sistema para comercio local: {escolha_3} votos
Votos válidos: {validos}
Votos inválidos: {invalidos}
''')

if validos > 0:
    percentual_1 = escolha_1 / validos * 100
    percentual_2 = escolha_2 / validos * 100
    percentual_3 = escolha_3 / validos * 100

    print(f'Desenvolvimento de jogos: {percentual_1:.2f}%')
    print(f'Aplicativo educacional: {percentual_2:.2f}%')
    print(f'Sistema para comercio local: {percentual_3:.2f}%')

    maior = max(escolha_1, escolha_2, escolha_3)

    if escolha_1 == maior and escolha_2 == maior and escolha_3 == maior:
        print('Houve empate entre os três projetos!')

    elif escolha_1 == maior and escolha_2 == maior:
        print('Houve empate entre desenvolvimento de jogos e aplicativo educacional!')

    elif escolha_1 == maior and escolha_3 == maior:
        print('Houve empate entre desenvolvimento de jogos e sistema para comercio local!')

    elif escolha_2 == maior and escolha_3 == maior:
        print('Houve empate entre aplicativo educacional e sistema para comercio local!')

    elif escolha_1 == maior:
        print('O tema vencedor foi desenvolvimento de jogos!')

    elif escolha_2 == maior:
        print('O tema vencedor foi aplicativo educacional!')

    elif escolha_3 == maior:
        print('O tema vencedor foi sistema para comercio local!')

else:
    print('Nenhum voto válido foi registrado!')


'''
• Qual valor será utilizado como sentinela?
O valor 0, pois ele encerra a votação.

• Quantos contadores serão necessários?
Serão necessários cinco contadores:
três para os votos de cada projeto, um para os votos válidos e um para os votos inválidos.

• Como identificar o maior número de votos?
Usando a função max() para descobrir qual dos três projetos possui mais votos.

• Como detectar um empate entre dois ou três temas?
Comparando a quantidade de votos de cada projeto com o maior número de votos.
Se dois ou três tiverem a mesma quantidade, existe empate.
'''

print('Exercício 4')
print('Controle de estacionamento')

ocupacao = 0
entradas = 0
saidas = 0
maior_ocupacao = 0
arrecadacao = 0

while True:
    print('''
[1]- Registrar entrada
[2]- Registrar saída
[3]- Consultar ocupação
[0]- Encerrar sistema
''')

    opcao = int(input('Sua escolha: '))

    if opcao == 1:
        if ocupacao >= 20:
            print('Estacionamento lotado!')
        else:
            ocupacao += 1
            entradas += 1

            if ocupacao > maior_ocupacao:
                maior_ocupacao = ocupacao

            print('Entrada registrada!')

    elif opcao == 2:
        if ocupacao <= 0:
            print('O estacionamento está vazio!')
        else:
            ocupacao -= 1
            saidas += 1
            arrecadacao += 8

            print('Saída registrada!')
            print('R$ 8,00 arrecadados!')

    elif opcao == 3:
        vagas_disponiveis = 20 - ocupacao

        print(f'Veículos no estacionamento: {ocupacao}')
        print(f'Vagas disponíveis: {vagas_disponiveis}')

    elif opcao == 0:
        print('Sistema encerrado!')

        print(f'''
Total de entradas: {entradas}
Total de saídas: {saidas}
Maior ocupação: {maior_ocupacao}
Valor arrecadado: R$ {arrecadacao:.2f}
''')
        break

    else:
        print('Essa opção não existe!')


'''
• Qual variável representa o estado atual do estacionamento?
A variável ocupacao, pois ela mostra quantos veículos estão atualmente no estacionamento.

• Que condições devem ser verificadas antes de uma entrada ou saída?
Antes da entrada, deve verificar se o estacionamento já está cheio.
Antes da saída, deve verificar se o estacionamento está vazio.

• Como registrar a maior ocupação?
Comparando a ocupacao atual com a maior_ocupacao e atualizando quando a ocupação for maior.

• Qual estrutura manterá o menu funcionando?
O while True mantém o menu funcionando até o usuário escolher a opção 0.
'''

print('Exercício 5')
print('Pesquisa de satisfação')

participantes = 0
soma_notas = 0

nota_1 = 0
nota_2 = 0
nota_3 = 0
nota_4 = 0
nota_5 = 0

while True:
    nota = int(input('Digite uma nota de 1 a 5 ou 0 para encerrar: '))

    if nota == 0:
        print('Pesquisa encerrada!')
        break

    elif nota == 1:
        nota_1 += 1
        participantes += 1
        soma_notas += nota

    elif nota == 2:
        nota_2 += 1
        participantes += 1
        soma_notas += nota

    elif nota == 3:
        nota_3 += 1
        participantes += 1
        soma_notas += nota

    elif nota == 4:
        nota_4 += 1
        participantes += 1
        soma_notas += nota

    elif nota == 5:
        nota_5 += 1
        participantes += 1
        soma_notas += nota

    else:
        print('Nota inválida! Digite uma nota de 1 a 5.')


if participantes > 0:

    media = soma_notas / participantes

    positivas = nota_4 + nota_5
    percentual_positivo = positivas / participantes * 100

    maior = max(nota_1, nota_2, nota_3, nota_4, nota_5)

    print(f'''
Total de participantes: {participantes}
Soma das notas: {soma_notas}
Média: {media:.2f}

Nota 1: {nota_1}
Nota 2: {nota_2}
Nota 3: {nota_3}
Nota 4: {nota_4}
Nota 5: {nota_5}

Avaliações positivas: {percentual_positivo:.2f}%
''')

    if maior == nota_1:
        print('A nota 1 foi uma das mais escolhidas!')

    if maior == nota_2:
        print('A nota 2 foi uma das mais escolhidas!')

    if maior == nota_3:
        print('A nota 3 foi uma das mais escolhidas!')

    if maior == nota_4:
        print('A nota 4 foi uma das mais escolhidas!')

    if maior == nota_5:
        print('A nota 5 foi uma das mais escolhidas!')

    if media < 2.5:
        print('Classificação: Avaliação negativa')

    elif media < 4:
        print('Classificação: Avaliação regular')

    else:
        print('Classificação: Avaliação positiva')

else:
    print('Nenhuma avaliação foi registrada!')


'''
• Qual valor será utilizado para encerrar a coleta?
O valor 0.

• Qual variável será o acumulador?
A variável soma_notas, pois ela acumula a soma de todas as notas.

• Quais contadores serão necessários?
Um contador para os participantes e cinco contadores para as notas de 1 a 5.

• Como evitar uma divisão por zero?
Verificando se participantes é maior que 0 antes de calcular a média e o percentual.

• Como identificar a nota mais escolhida?
Usando a função max() para encontrar a maior quantidade de escolhas e comparando cada contador com esse valor.
'''

'''
Justificativa da escolha entre for e while:

Escolhi o while porque as repetições dependem de uma condição de encerramento.
Na questão 3, a votação termina quando o usuário digita 0.
Na questão 4, o menu continua até o usuário escolher 0.
Na questão 5, a pesquisa continua até o usuário digitar 0.
'''