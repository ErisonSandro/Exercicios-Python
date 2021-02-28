temp = []
prin = []
maior = menor = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))

    if len(prin) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] >= maior:
            maior = temp[1]
        if temp[1] <= menor:
            menor = temp[1]

    prin.append(temp[:])
    temp.clear()


    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    if cont == 'N':
        break


print('=-' * 30)
print(f'Ao todo, voce cadastrou {len(prin)} pessoas')
print(f'O maior peso foi de {maior}kg peso de ', end='')
for p in prin:
    if p[1] == maior:
        print(f'[{p[0]}]', end='  ')
print(f'\nO menor peso foi de {menor}kg peso de ', end='')
for p in prin:
    if p[1] == menor:
        print(f'[{p[0]}]', end='  ')
