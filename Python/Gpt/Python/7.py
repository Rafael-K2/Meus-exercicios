total = 0
num_selecionados = 0
maior = 0
menor = 1000
while True:
    clcv = int(input('Quanto vc quer colocar: '))
    total += clcv
    num_selecionados += 1
    if clcv == 0:
        num_selecionados -=1
        break
    if clcv > maior:
        maior = clcv
    if clcv < menor:
        menor = clcv
print(f'Você colocou {num_selecionados} Valores, e a soma deles deu {total}.\nO maior foi {maior} e o menor foi {menor}')