from datetime import date
maior = 0
menor = 0
for cont in range(1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(cont)))
    atual = date.today().year
    idade = atual - ano
    if idade > 18:
        maior += 1
    else:
        menor = menor + 1

print('Ao todo tivemos {} pessoas maiores de idade'.format(maior))
print('Ao todo tivemos {} pessoas menores de idade'.format(menor))
