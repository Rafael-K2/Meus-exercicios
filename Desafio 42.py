r1 = int(input('primeiro segmento:'))
r2 = int(input('segundo segmento:'))
r3 = int(input('terceiro segmento:'))

if r1 == r2 == r3:
    print('Triangulo equilatero')
elif r1 > r2 == r3:
    print('Isosceles')
elif r1 != r2 != r3:
    print('Escaleno')