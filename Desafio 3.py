n1 =int(input ('Primeiro número'))
n2 =int(input ('Segundo número'))
operação = input('Escolha a operação: + - * /')
s = n1+n2
if operação == '+':
    print(n1+n2)
elif operação == '-':
    print(n1-n2)
elif operação == '/':
    print(n1/n2)
elif operação == '*':
    print(n1*n2)

'''Para a "calculadora funcionar de forma correta,
 usa-se "int" antes de "input" para que o input
seja realmente um numero.'''