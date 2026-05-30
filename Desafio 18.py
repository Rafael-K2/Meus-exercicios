'''
print('Esse programa diz o seno e cosseno dos angulos de 30, 45 é 60')
p = int(input('Angulo q vc quer:'))
if p == 30:
    print('seno é 1/2\ncosseno é √3/2')
elif p == 45:
    print('seno é √2/2\ncosseno é √2/2')
elif p == 60:
    print('seno é √3/2 cosseno 1/2')
else:
    print('O angulo q vc escolheu não é nenhuma das opções disponiveis')
    "Meu código"
'''
import math
an = float(input('Angulo:'))
s= math.sin(math.radians(an))
c= math.cos(math.radians(an))
t= math.tan(math.radians(an))
print('Sen{:.2f}\nCos{:.2f}\nTan{:.2f}'.format(s,c,t))
