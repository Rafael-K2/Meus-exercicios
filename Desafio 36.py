valor_da_casa = float(input('Qual o valor da casa ?'))
salário = float(input('Qual seu salário ?'))
anos = int(input('Vai pagar em quantos anos ?'))
pagamento = valor_da_casa / (anos * 12 )
if pagamento <= 30/100:
    print( 'vc n pode comprar essa casa')
else:
    print('só mandar o pix')