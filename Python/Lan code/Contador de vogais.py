palavra = input('Qual palavra você quer contar as vogais? ').lower()

vogais = 'aeiou'
total_vogais = 0

for letra in palavra:
    if letra in vogais:
        print(f"Vogal encontrada: {letra}")
        total_vogais += 1
print(f"O total de vogais na palavra é: {total_vogais}")
