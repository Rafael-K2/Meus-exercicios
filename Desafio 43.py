print('Indice de massa corporea')

i = float(input('Qual seu IMC ?'))
if i <= 18.5:
    print('Baixo')
elif i <= 18.5 < 25:
    print('Normal')
elif i >= 25 <= 40:
    print('Obesidade')
elif i > 40:
    print('Obesidade morbida')